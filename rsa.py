

#CONSANTS
alphabet_dict = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVXYZ0123456789~!@#$%^&*()_-+=|\\:;\"',.?/"
prime1 = 19175002942688032928599
prime2 = 7369130657357778596659
public_key = 239

n = prime1*prime2
public_tuple = (prime1*prime2,public_key)


def sequencer(a):
	# takes a value from alphabet_dict string and returns a numeric value between 10 and 95 inclusive
	return alphabet_dict.index(a) + 10

def encoder(s):
	# takes string and returns numerical representation
	encoded_digit = ""
	for i in s:
		encoded_digit = encoded_digit + (str(sequencer(i)))
	return encoded_digit

def interpreter(r):
	return (alphabet_dict[r-10])

def decoder(m):
	# takes numerical representation and returns string
	decoded_message = ""
	for i in range(0,len(m),2):
		decoded_message = decoded_message + interpreter(int(m[i:i+2])) 
	return decoded_message

def eea(c,d):
	if c == d:
		print("They're equal")
	elif c > d:
		a = d
		m = c
	elif c < d:
		a = c
		m = d

	m1 = 1
	m2 = 0
	m3 = 0
	m4 = 1
	r = 1
	while r != 0:
		if a < m:
			q = m//a  # setting quotient
			r = m-(q*a)  # setting remainder
			m = r  

			m1 = m1-(m3*q)
			m2 = m2-(m4*q)

		elif a > m:
			q = a//m
			r = a-(q*m)
			a = r

			m3 = m3-(m1*q)
			m4 = m4-(m2*q)

	if a == 0:
		alpha = m1
		beta = m2
		gcd = m
	elif m == 0:
		alpha = m3
		beta = m4
		gcd = a

	#print("alpha: "+str(alpha)+" beta: "+str(beta)+" gcd: "+str(gcd))
	return alpha, beta, gcd

def encryption_algorithm(m,e,n):
	# encryption algorithm
	return pow(m,e,n)

def encrypter(m):
	# Takes n and public key, returns encrypted numerical list representation
	e = int(input("Insert your public key: "))
	return encryption_algorithm(int(m),e,n)

def decryption_algorithm(c,d,n):
	# decryption algorithm
	return pow(c,d,n)

def decrypter(c,d):
	# Takes encrypted message c and private key d, returns decrypted numerical list representation 
	return str(decryption_algorithm(int(c),d,n))

def get_private_key(e):
	# Calculates and returns private key
	phi = (prime1-1)*(prime2-1)
	d = eea(e, phi)[1]  # private key
	while d<0:  # making sure the private key is the smallest positive residue
		d = d+phi
	if (d*e)%phi != 1:
		print("There is something wrong, as your private and public keys are not inverses in mod phi.")
	return d
			
def send(message):
	# Takes message and implements rsa encryption 
	n = prime1 * prime2
	phi = (prime1-1) * (prime2-1)
	e = public_key  
	
	print("Message: "+message)
	encrypted_message = encrypter(encoder(message))
	print("Encrypted message: ", end="") 
	print(encrypted_message)

def receive(received,d):
	# Takes encrypted message and implements rsa decryption
	print()
	print("Received encryption: ", end="")
	print(received) 
	message = decoder(decrypter(received,d))
	print("Message received: " + message)

def main():

	print("Entering public channel;")
	print("n: " + str(public_tuple[0]))
	print("Public key: " + str(public_tuple[1]))
	print()
	accuracy = len(str(prime1*prime2))/2-1
	print("Current prime security allows for a maximum of " + str(int(accuracy)) + " character messages.")
	print()
	access_key = input("If you are a channel moderator, enter access key: ")
	if access_key=="666": 
		print("Channel private key: " + str(get_private_key(public_key)))
	else:
		print("Access key incorrect.")

	iter = 0
	action = 3
	while action != 0:
		print()
		print()
		action = int(input("Would you like to send or receive?(send;1 , receive;2 , exit; 0): "))
		if action == 1:
			message = input("Relay your message: ")
			send(message)
		elif action == 2:
			iter = iter + 1
			encryption = input("Relay your encrypted message: ")
			if iter == 1:
				private_key = int(input("Relay your personal private key(make sure no one is looking): "))
			receive(encryption,private_key)
			
main()













