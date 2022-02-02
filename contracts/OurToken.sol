// contracts/OurToken.sol
// SPDX-License-Identifier: MIT
pragma solidity ^0.7.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract OurToken is ERC20 {
    constructor(uint256 initialSupply) ERC20("GOLDEN_TOAD", "GTOAD") {
        _mint(msg.sender, initialSupply);
    }
}
