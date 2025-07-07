async function main() {
  const DrainMe = await ethers.getContractFactory("DrainMe");
  const contract = await DrainMe.deploy();
  await contract.deployed();

  console.log("Contract deployed to:", contract.address);
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error(error);
    process.exit(1);
  });
