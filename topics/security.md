## Encryption algorithms

	- attributes:
		- one computationally expensive operation (find prime or curve used to calculate a number, longer key sizes)
		- non-linear relationships

	- requirements:
		- confidentiality
		- authenticity

	- common core operations:
		- xor
		- substitution
		- affine map
		- permutation

	- concepts:
		- order
		- symmetry
		- random
		- substitution :: map
		- permutation :: combination
		- division :: group

	- attack types from wiki:
		- related key attack
		- known key distinguishing attack
		- key recovery attack
		- biclique attack
		- side channel attacks: attack on data leakage in software or hardware implementations
			cache-timing:
			differential fault analysis: introduce unexpected conditions to reveal internal states within an encryption implementation
		- linear cryptanalysis
		- differential cryptanalysis
		- truncated differential cryptanalysis
		- partial differential cryptanalysis
		- integral cryptanalysis, which encompasses square & integral attacks
		- slide attacks
		- boomerang attacks
		- XSL attack
		- impossible differential cryptanalysis
		- algebraic attacks


risk = threats x vulnerabilities x consequences

security attributes:
	confidentiality: privacy
	integrity: editability
	availability: access, retainment vs. destruction
	possession: ownership
	utility: usefulness
	authenticity: legitimacy

non-repudiation: inability to deny having received/sent message
authentication: verifies identity of user
authorization: upon authentication, what is it allowed to access (permissions)

defense in depth layers:
- prevention
- detection
- recovery
- risk probability alerts for action on each feature given recent exploits
- give hackers' each others' contact information so they only hack each other and it forms a closed trade loop independent of the economy


virus types:
- macro: usually written in platform-independent language, embedded in docs, usually activated on opening document
- stealth: hides modifictions, trick antivirus into accepting intercepted requests to os
- polymorphic: produces variable copies of itself
- self-garbling: modifies its code to avoid identification
- bots: hacked devices under control of a hacker
- worms: spread from one machine to another
- os root kits: usually embedded in os kernel to hide
- firmware kits: embedded in firmware, can do things like reformatting your drive so the os cant be reinstalled
	- persistence means itll survive a reinstall of the os
- trojan horses: executes malicious code while performing legitimate functions
- rat (remote access tool): allow others to access your system remotely
- key logger: tracks key events
- cpu hijackers

attack types:
- drive-by attacks
- script injection/redirection in adware
- adware forces ads
- scareware: makes user think an attack has happened to trigger an action
- potentially unwanted programs: antivirus cant tell if its intentional installation/download
- cross-site-scripting vulnerability

- hybrid encryption uses symmetric algorithm to encrypt data & asymmetric algorithm to encrypt key exchange
- tls, https over tls, & pgp use hybrid encryption
- digital signature is a hash value encrypted private key, protecting from changes after exchange and authenticating sender

SSL/TLS handshake:
    1. client sends a message to the server
    2. server sends the public key or certificate
    3. client checks public key or certificate
    	4.a if public key or certificate found/valid, client creates a symmetric key
    		5. client sends symmetric key to server (using asymmetric encryption to protect key exchange)
    			6. server encrypts requested data with symmetric key
    				7. client decrypts response data with symmetric key
    	4.b if public key or certificate not found/valid, the communication fails
    
SSL encryption
	- uses symmetric encryption to encrypt data between client & server
	- uses asymmetric encryption to exchange generated symmetric key (validates identity of client & server)
	- asymmetric encryption protects key exchange

		- Public key encryption is used to exchange the symmetric key between client & server
	- symmetric encryption protects data exchange, once symmetric key is distributed to both

Asymmetric vs. symmetric encryption
	- symmetric cryptography
		- single key for encryption/decryption
		- pre-shared key encryption algorithms: Twofish, AES, or Blowfish
			- symmetric key used to encrypt data between client & server

	- asymmetric cryptography
		- public/private key for encryption/decryption
		- public key encryption algorithms: ECC, RSA

Certificate Signing Request (CSR)
	- base64-encoded metadata (like name/email) used by certifying authority (CA) to issue SSL certificate to the user

Certificate Authentication Level (AL)
	- Authentication level: trustworthiness of a hosted URL
		- Domain Validation (DV): CA verifies if the domain is controlled by an organization, can be done via email
		- Organization Validation (OV): CA validates the name, state, & country of an organization, by physically verifying organization location
		- Extended Validation (EV): CA validates ownership, physical location, state, & country of organization, by physically verifying organization location & checking company legal existence