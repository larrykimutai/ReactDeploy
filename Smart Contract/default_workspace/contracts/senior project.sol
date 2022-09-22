// SPDX-License-Identifier: MIT
pragma solidity >= 0.5.1;

contract MyContract{
    address payable wallet;
    uint Dcounter;
    

    constructor (address payable _wallet) {
        wallet = _wallet;
    }

    struct donor{
            uint totalDono;
            uint returnedDono;
            uint donorListPointer;
    }

    mapping(address => donor) public balances;
    address[] public donorList;

    event LogReceivedFunds(address sender, uint amount);
    event LogReturnedFunds(address recipient, uint amount);

    function getDonorCount()
        public 
        returns(uint donorCount){
        return donorList.length;
        }
    
    

    function donate() public payable{
        //balances[msg.sender] += 1;
        balances[msg.sender].totalDono += msg.value;
        balances[msg.sender].donorListPointer = Dcounter++;
        donorList.push(msg.sender);
        emit LogReceivedFunds(msg.sender, msg.value);
    }

    //this function sends the funds after requirements are met
    function sendFunds () public{
        wallet.transfer(balances[msg.sender].totalDono); 
        //balances[msg.sender].totalDono = 0;
    }

    //this function returns funds after requirements are not met
    function returnFunds() public payable{
        balances[msg.sender].returnedDono += msg.value;
        emit LogReturnedFunds(msg.sender, msg.value);
    }

}