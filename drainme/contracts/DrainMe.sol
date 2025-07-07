// Directory: drainme-ctf
// File: contracts/DrainMe.sol

// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

contract DrainMe {
    mapping(address => uint256) public balances;

    function deposit() public payable {
        balances[msg.sender] += msg.value;
    }

    function withdraw() public {
        require(balances[msg.sender] > 0, "Nothing to withdraw");

        (bool success, ) = msg.sender.call{value: balances[msg.sender]}("");
        require(success, "Failed to send Ether");

        balances[msg.sender] = 0;
    }

    function getBalance() public view returns (uint256) {
        return address(this).balance;
    }
}
