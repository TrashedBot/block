pragma solidity ^0.4.24;


contract TRASHED_DAO is ERC223Token {
    using SafeMath for uint256;
    string public name = "Trashed DAO Token";
    string public symbol = "TRASH";
    uint public decimals = 4;
    uint public totalSupply = 7700000000 * (10**decimals);
    address private treasury = 0xcFd3742D0013eFB98A84b94B7BedF0315BC0413D;
    uint256 private priceDiv = 2000000000;
    event Purchase(address indexed purchaser, uint256 amount);
    constructor() public {
    balances[msg.sender] = 900000000 * (10**decimals);
    balances[0x0] = 100000000 * (10**decimals);}
    function () public payable {
        bytes memory empty;
        if (msg.value == 0) { revert(); }
        uint256 purchasedAmount = msg.value.div(priceDiv);
        if (purchasedAmount == 0) { revert(); }
        if (purchasedAmount > balances[0x0]) { revert(); }
        treasury.transfer(msg.value);
        balances[0x0] = balances[0x0].sub(purchasedAmount);
        balances[msg.sender] = balances[msg.sender].add(purchasedAmount);
        emit Transfer(0x0, msg.sender, purchasedAmount);
        emit ERC223Transfer(0x0, msg.sender, purchasedAmount, empty);
        emit Purchase(msg.sender, purchasedAmount);
    }
}

TRASHED_DAO.sol
