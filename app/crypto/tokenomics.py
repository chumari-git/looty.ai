from web3 import Web3

class LootyToken:
    def __init__(self, rpc_url):
        self.web3 = Web3(Web3.HTTPProvider(rpc_url))

    def create_token(self, name, symbol, total_supply):
        """Deploy a basic ERC-20 token."""
        # ERC-20 contract code simplified for demonstration
        contract_code = """
        pragma solidity ^0.8.0;
        contract LootyToken {
            string public name = "<name>";
            string public symbol = "<symbol>";
            uint8 public decimals = 18;
            uint256 public totalSupply;
            mapping (address => uint256) public balanceOf;

            constructor(uint256 _initialSupply) {
                totalSupply = _initialSupply;
                balanceOf[msg.sender] = _initialSupply;
            }
        }
        """
        # Token creation process...
