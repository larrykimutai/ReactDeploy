require('dotenv').config();
const alchemyKey = process.env.REACT_APP_ALCHEMY_KEY;
const { createAlchemyWeb3 } = require("@alch/alchemy-web3");
const web3 = createAlchemyWeb3(alchemyKey);

const contractABI = require("../backend/contract-abi.json");
const contractAddress = "0xd1E3D3Bb0418e7Af816084F9F2B8eC9949FdbcB3";

export const helloWorldContract = new web3.eth.Contract(
    contractABI,
    contractAddress
);

// const { CallerContract } = require('web3-eth-contract');
// CallerContract.setProvider('wss://eth-goerli.g.alchemy.com/v2/y7PVXGDkWx1F_olSlXCEwVz2ayltSG3J');
// const callerContract = new CallerContract(contractABI, contractAddress);



// export const loadCurrentMessage = async () => {
//     const message = await helloWorldContract.methods.message().call();
//     return message;
// };

export const connectWallet = async () => {
    if (window.ethereum) {
        try {
            const addressArray = await window.ethereum.request({
                method: "eth_requestAccounts",
            });
            const obj = {
                status: "👆🏽 Write a message in the text-field above.",
                address: addressArray[0],
            };
            return obj;
        } catch (err) {
            return {
                address: "",
                status: "😥 " + err.message,
            };
        }
    } else {
        return {
            address: "",
            status: (
                <span>
          <p>
            {" "}
              🦊{" "}
              <a target="_blank" href={`https://metamask.io/download.html`}>
              You must install Metamask, a virtual Ethereum wallet, in your
              browser.
            </a>
          </p>
        </span>
            ),
        };
    }
};

export const getCurrentWalletConnected = async () => {
    if (window.ethereum) {
        try {
            const addressArray = await window.ethereum.request({
                method: "eth_accounts",
            });
            if (addressArray.length > 0) {
                return {
                    address: addressArray[0],
                    status: "👆🏽 Write a message in the text-field above.",
                };
            } else {
                return {
                    address: "",
                    status: "🦊 Connect to Metamask using the top right button.",
                };
            }
        } catch (err) {
            return {
                address: "",
                status: "😥 " + err.message,
            };
        }
    } else {
        return {
            address: "",
            status: (
                <span>
          <p>
            {" "}
              🦊{" "}
              <a target="_blank" href={`https://metamask.io/download.html`}>
              You must install Metamask, a virtual Ethereum wallet, in your
              browser.
            </a>
          </p>
        </span>
            ),
        };
    }
};

export const approve = async () =>{

    const addressArray = await window.ethereum.request({
        method: "eth_accounts",
    });

    const transParam = {
        to: contractAddress,
        from: addressArray[0],
        data: helloWorldContract.methods.sendFunds().encodeABI(),
    };

    const txHash = await window.ethereum.request({
        method: "eth_sendTransaction",
        params: [transParam],
    });
};

export const deny = async () =>{
    const addressArray = await window.ethereum.request({
        method: "eth_accounts",
    });

    const transParam = {
        to: contractAddress,
        from: addressArray[0],
        data: helloWorldContract.methods.singleRefund().encodeABI(),
    };

    const txHash = await window.ethereum.request({
        method: "eth_sendTransaction",
        params: [transParam],
    });
};


export const donate = async (address, userin) => {

    const userInput = (userin * Math.pow(10, 18)).toString(16);
    alert(userInput);


    const transParam = {
        to: contractAddress,
        from: address,
        value: userInput,
        data: helloWorldContract.methods.donate().encodeABI(),
    };

    alert("Starting transaction");
    const txHash = await window.ethereum.request({
        method: "eth_sendTransaction",
        params: [transParam],
        //value: userInput.toString(),
    });

    alert("IT WORKS!!!!");
}


// export const updateMessage = async (address, message) => {
//
//     //input error handling
//     if (!window.ethereum || address === null) {
//         return {
//             status:
//                 "💡 Connect your Metamask wallet to update the message on the blockchain.",
//         };
//     }
//
//     if (message.trim() === "") {
//         return {
//             status: "❌ Your message cannot be an empty string.",
//         };
//     }
//     //set up transaction parameters
//     const transactionParameters = {
//         to: contractAddress, // Required except during contract publications.
//         from: address, // must match user's active address.
//         data: helloWorldContract.methods.update(message).encodeABI(),
//     };
//
//     //sign the transaction
//     try {
//         const txHash = await window.ethereum.request({
//             method: "eth_sendTransaction",
//             params: [transactionParameters],
//         });
//         return {
//             status: (
//                 <span>
//           ✅{" "}
//                     <a target="_blank" href={`https://ropsten.etherscan.io/tx/${txHash}`}>
//             View the status of your transaction on Etherscan!
//           </a>
//           <br />
//           ℹ️ Once the transaction is verified by the network, the message will
//           be updated automatically.
//         </span>
//             ),
//         };
//     } catch (error) {
//         return {
//             status: "😥 " + error.message,
//         };
//     }
// };
