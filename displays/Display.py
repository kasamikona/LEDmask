import asyncio

class Display():
	@classmethod
	async def connect(cls, addresses=None):
		'''
		Attempts to connect to an appropriate device.
		May be given specific addresses to check.
		Returns object: New instance of this display if connected, otherwise None.
		'''
		return None

	async def disconnect(self):
		'''Disconnects the connected device'''
		pass

	def __init__(self):
		self.width = 0
		self.height = 0
		self.color = False # RGB or monochrome display
		self.bit_depth = 1 # Total bits per pixel
		self.buffer = None # Pixel buffer
		self.bit_remap = None # Reverse map output bits into pixel buffer
		self.max_fps = 0 # Max frame rate the display/connection can handle, should be slightly below measured maximum
		self.is_connected = False

	def reverse_map_bit(self, bit):
		'''
		Returns tuple: Reverse map a bit position in the output stream to an (x, y, bit) location in the pixel buffer.
		Must return 0 <= x < width, 0 <= y < height, 0 <= bit < bit_depth. Zeroth bit is LSB of last channel.
		'''
		return (0, 0, 0) # x, y, c

	def generate_buffer(self):
		self.buffer = [[0]*self.height for x in range(self.width)]

		num_bits = self.width * self.height * self.bit_depth
		self.num_bits = num_bits

		self.bit_remap = [0]*num_bits
		for i in range(num_bits):
			self.bit_remap[i] = self.reverse_map_bit(i)

	def get_output_bytes(self):
		num_bytes = (self.num_bits + 7) // 8
		out_bytes = bytearray(num_bytes)
		for i in range(num_bytes):
			bv = 0
			for j in range(8):
				bv += bv
				if (i*8)+j < self.num_bits:
					map = self.bit_remap[(i*8)+j]
					bv += (self.buffer[map[0]][map[1]] >> map[2]) & 1
			out_bytes[i] = bv
		return out_bytes

	async def prepare(self):
		pass

	async def clear(self, send=True, wait_response=False):
		for x in range(self.width):
			for y in range(self.height):
				self.buffer[x][y] = 0
		if send:
			await self.send(wait_response)

	async def send(self, wait_response=False):
		out_bytes = self.get_output_bytes()
		await self.write_data_start(len(out_bytes))
		while len(out_bytes) > 0:
			num_written_bytes = await self.write_more_data(out_bytes)
			out_bytes = out_bytes[num_written_bytes:]
		await self.write_data_end(wait_response)

	async def write_data_start(self, length):
		pass

	async def write_data_end(self, wait_response):
		pass

	async def write_more_data(self, data):
		return 1

	async def wait_for_finish(self):
		pass

	async def start_notify_ack(self):
		pass

	async def stop_notify_ack(self):
		pass
