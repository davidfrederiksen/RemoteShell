import getpass
import telnetlib
import paramiko
class RSH:
	connection = 'false'
	ssh = paramiko.SSHClient()
	tn = ''

	def remote_connect(self):
		HOST = input("Enter Hostname or IP: ")
		user = input("Enter your remote account: ")
		password = getpass.getpass()
		try:
			self.ssh.load_system_host_keys()
			self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
			self.ssh.connect(HOST.encode('ascii'), username=user.encode('ascii'), password=password.encode('ascii'))
			self.connection = 'SSH'
		except:
			try:
				self.tn = telnetlib.Telnet(HOST)
				listindex, match, bytes = self.tn.expect(['Username', 'Password'])
				if listindex == 0:
					self.tn.write(user.encode('ascii') + b"\n")
					self.tn.read_until(b"Password: ")
					self.tn.write(password.encode('ascii') + b"\n")
				elif listindex == 1:
					self.tn.read_until(b"Password: ")
					self.tn.write(password.encode('ascii') + b"\n")
				self.connection = 'telnet'
				print('Telnet')
			except:
				print("Remote Login failed.")
				self.connection = 'false'
			
	def run_command(self, command):
		if self.connection == 'false':
			print("Error: No connection to send command to.")
			return "Error: No connection to send command to."
		print(self.connection.encode('ascii'))
		if self.connection == 'SSH':
			stdin, stdout, stderr = self.ssh.exec_command(command)
			output = stdout.read()
		elif self.connection == 'telnet':
			print("Running command in Telnet")
			self.tn.write(command.encode('ascii') + b"\n")
			output = self.tn.read_until('"')
		return output

	def close_connection(self):
		if self.connection == 'SSH':
			self.ssh.close()
		elif self.connection == 'telnet':
			self.tn.close()

	