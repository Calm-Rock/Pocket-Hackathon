# Pocket-Hackathon
This is a submission for [Pocket Network DAO Global Bounty](https://gitcoin.co/issue/pokt-foundation/bounties/3/100026898) on Gitcoin.

You can see the live demo [here](https://pocket-hackathon-app.herokuapp.com/)

A short video demo is available [here](https://drive.google.com/drive/folders/1f_iDEQkiiZhb4kRzGwCfZCKUHazXWzxQ?usp=sharing)

This dApp uses the RPC endpoint minted from the Pokt portal to find the basic details of a transaction on Ethereum Blockchain.
It's created using the streamlit python library.

Shortcomings
- If after a certain interval the transaction details are not given in the search bar then the app will throw an error. After putting the trnsaction hash detail in the search bar it works smootly. I will integrate a logic to handle this error in future improvements
