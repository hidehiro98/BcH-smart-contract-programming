pragma solidity ^0.4.8;

import "contracts/MyToken.sol";
import "contracts/IndivisibleAsset.sol";

contract OneTimeEscrow {

    MyToken _token;
    IndivisibleAsset _asset;

    address public _buyer;
    address public _seller;
    uint256 public _price;

    event AssetRetrieved();
    event TokenRetrieved();
    event Settled();

    function OneTimeEscrow(address token, address buyer,
     address asset, address seller, uint256 price) {

        _token = MyToken(token);
        _asset = IndivisibleAsset(asset);

        _buyer = buyer;
        _seller = seller;
        _price = price;
    }

    function retrieveAsset() {

        address addr = this;

        if (_asset.getOwner() != addr) {
            throw;
        }

        _asset.transfer(_seller);

        AssetRetrieved();
    }

    function retrieveToken() {

        if (_token.getBalanceOf(this) < _price) {
            throw;
        }

        _token.transfer(_buyer, _price);

        TokenRetrieved();
    }

    function settle() {

        address addr = this;

        if (_token.getBalanceOf(this) < _price || _asset.getOwner() != addr) {
            throw;
        }

        // send the token (coin) to the seller
        _token.transfer(_seller , _price);
        // send the asset to the buyer
        _asset.transfer(_buyer);

        // logging the events
        Settled();
    }
}

/* end of OneTimeEscrow.sol */
