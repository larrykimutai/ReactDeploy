// SPDX-License-Identifier: MIT
pragma solidity >= 0.5.1;

contract MyContract{
    address payable wallet;
    uint Dcounter;
    uint deployDate;//start date
    uint deadline;//the amount of weeks the project will take
    //this boolean represents user approval of work done
    bool approved = false;

    constructor (address payable _wallet, uint numWeeks) {
        wallet = _wallet;
        deployDate = block.timestamp;
        deadline = numWeeks;
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
/*
    function getDonorCount()
         public 
        returns(uint donorCount){
        return donorList.length;
        }
    */

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
        balances[msg.sender].returnable = 0;
    }

    function singleRefund () public{
        uint returnAmt = balances[msg.sender].returnable;
        payable (msg.sender).transfer(returnAmt);
        emit LogReturnedFunds(msg.sender, returnAmt);
    } 

    //this function returns funds if requirements are not met
    function returnFunds() private {
        for(uint i; i <= donorList.length-1; i++){
            uint returnAmt;
            //checks if the user has any ether remaining in the contract 
            if(balances[donorList[i]].returnable > 0){
                returnAmt = balances[donorList[i]].returnable;
                donorList[i].transfer(returnAmt);
                balances[donorList[i]].returnedDono = returnAmt;
                balances[donorList[i]].returnable = 0;
                emit LogReturnedFunds(donorList[i], returnAmt);
                }
            }
        }
    
    function approval() private{       
      require(msg.sender == wallet);
        approved = true;
    }

    function timeExpired() public {
        //checks if the time expired and the creator uploaded proof of work
        if(block.timestamp >= (deployDate + (deadline * 1 weeks))
        && approved == true){
            selfdestruct(wallet);
        }
    //the refund function is called if the deadline is met
        else if (block.timestamp >= (deployDate + (deadline * 1 weeks))
        && approved == false){
            returnFunds();
    }
  }


}