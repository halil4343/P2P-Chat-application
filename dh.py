import random

def generate_shared_key(p, g, private_key, their_public_key):
    """
    Generate shared key using Diffie-Hellman
    p: prime number
    g: generator
    private_key: our private key
    their_public_key: their public key
    """
    return (their_public_key ** private_key) % p