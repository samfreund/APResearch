import math

def calculate_entropy(password):
    # Define the character sets
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    special_characters = "!@#$%^&*()-_=+[{]}\\|;:'\",<.>/?`~"  # Common special characters
    
    # Determine character set based on password content
    charset_size = 0
    if any(char in lowercase for char in password):
        charset_size += len(lowercase)
    if any(char in uppercase for char in password):
        charset_size += len(uppercase)
    if any(char in digits for char in password):
        charset_size += len(digits)
    if any(char in special_characters for char in password):
        charset_size += len(special_characters)
    
    # Calculate entropy per character
    if charset_size == 0:
        return 0  # No valid characters found
    entropy_per_char = math.log2(charset_size)
    
    # Total entropy
    total_entropy = entropy_per_char * len(password)
    
    return total_entropy

def main():
    #loop through json dict and then update with entropy values