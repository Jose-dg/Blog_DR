require("@nomicfoundation/hardhat-toolbox");
// require("@nomicfoundation/hardhat-web3");
require("@nomiclabs/hardhat-web3");
require("dotenv").config();

/** @type import('hardhat/config').HardhatUserConfig */
module.exports = {
  solidity: "0.8.18",
  paths: {
    artifacts: "./src/cache",
  },
  networks: {
    hardhat: {
      chainId: 31337
    }
  }
};


