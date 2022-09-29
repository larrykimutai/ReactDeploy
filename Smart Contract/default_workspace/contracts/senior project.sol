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
            uint returnable;
            uint donorListPointer;
    }

    mapping(address => donor) public balances;
    address payable[] public donorList;

    event LogReceivedFunds(address sender, uint amount);
    event LogReturnedFunds(address recipient, uint amount);

    function getDonorCount()
        public 
        returns(uint donorCount){
        return donorList.length;
        }
    

    function donate() public payable{
        balances[msg.sender].totalDono += msg.value;
        balances[msg.sender].returnable += msg.value;
        balances[msg.sender].donorListPointer = Dcounter++;
        donorList.push(payable(msg.sender));
        emit LogReceivedFunds(msg.sender, msg.value);
    }

    //this function sends the funds after requirements are met
    function sendFunds () public{
        wallet.transfer(balances[msg.sender].totalDono); 
        balances[msg.sender].returnable == 0;
    }

    //this function returns funds if requirements are not met
    function returnFunds() public payable{
        for(uint i; i < donorList.length-1; i++){
            //checks if the user has any ether remaining in the contract 
            if(balances[donorList[i]].returnable > 0){
                donorList[i].transfer(balances[donorList[i]].returnable);
                balances[donorList[i]].returnedDono == balances[msg.sender].totalDono;
                balances[donorList[i]].returnable == 0;
            }
        }
        emit LogReturnedFunds(msg.sender, msg.value);
    }

}