import React from "react";
import { useEffect, useState } from "react";
import {
    helloWorldContract,
    connectWallet,
    updateMessage,
    loadCurrentMessage,
    getCurrentWalletConnected,
} from "./util/interact.js";



import alchemylogo from "./alchemylogo.svg";

const HelloWorld = () => {
    //state variables
    const [walletAddress, setWallet] = useState("");
    const [status, setStatus] = useState("");
    const [message, setMessage] = useState("No connection to the network."); //default message
    const [newMessage, setNewMessage] = useState("");

    //called only once
    useEffect(async () => {
        const message = await loadCurrentMessage();
        setMessage(message);
        addSmartContractListener();

        const {address, status} = await getCurrentWalletConnected();
        setWallet(address);
        setStatus(status);

        addWalletListener();
    }, []);

    function addSmartContractListener() {
        helloWorldContract.events.UpdatedMessages({}, (error, data) => {
            if (error) {
                setStatus("😥 " + error.message);
            } else {
                setMessage(data.returnValues[1]);
                setNewMessage("");
                setStatus("🎉 Your message has been updated!");
            }
        });

    }

    function addWalletListener() { //TODO: implement

        if (window.ethereum) {
            window.ethereum.on("accountsChanged", (accounts) => {
                if (accounts.length > 0) {
                    setWallet(accounts[0]);
                    setStatus("👆🏽 Write a message in the text-field above.");
                } else {
                    setWallet("");
                    setStatus("🦊 Connect to Metamask using the top right button.");
                }
            });
        } else {
            setStatus(
                <p>
                    {" "}
                    🦊{" "}
                    <a target="_blank" href={`https://metamask.io/download.html`}>
                        You must install Metamask, a virtual Ethereum wallet, in your
                        browser.
                    </a>
                </p>
            );
        }
    }

    const connectWalletPressed = async () => {
        const walletResponse = await connectWallet();
        setStatus(walletResponse.status);
        setWallet(walletResponse.address);
    };

    const onUpdatePressed = async () => { //TODO: implement
        const { status } = await updateMessage(walletAddress, newMessage);
        setStatus(status);
    };



    //the UI of our component
    return (
        <div id="container">
            {/*<img id="logo" src={alchemylogo}></img>*/}
            <button id="walletButton" onClick={connectWalletPressed}>
                {walletAddress.length > 0 ? (
                    "Connected: " +
                    String(walletAddress).substring(0, 6) +
                    "..." +
                    String(walletAddress).substring(38)
                ) : (
                    <span>Connect Wallet</span>
                )}
            </button>

            <h2 style={{ paddingTop: "50px" }}>Progress:</h2>
            {/*<p>{message} </p>*/}
            {/*<img src={logo}/>*/}


            <h2 style={{ paddingTop: "18px" }}>Enter Amount:</h2>

            <div>
                <input
                    type="text"
                    placeholder="Enter amount in Ether."
                    onChange={(e) => setNewMessage(e.target.value)}
                    value={newMessage}
                />
                {/*<p id="status">{status}</p>*/}
                <p>You donated: {message} Ether</p>

                <button id="publish" onClick={onUpdatePressed}>
                    Donate
                </button>
                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                <button id="publish">Approve</button>
                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                <button id="publish">Deny</button>
            </div>
        </div>
    );
};

export default HelloWorld;
