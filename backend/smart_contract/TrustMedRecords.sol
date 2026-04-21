// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract TrustMedRecords {

    struct Record {
        uint256 recordId;
        string userId;
        string predictionHash;
        string riskLevel;
        string modelVersion;
        uint256 timestamp;
    }

    uint256 public recordCount;

    mapping(uint256 => Record) public records;

    event RecordStored(
        uint256 recordId,
        string userId,
        string predictionHash,
        string riskLevel,
        string modelVersion,
        uint256 timestamp
    );

    function storeRecord(
        string memory _userId,
        string memory _predictionHash,
        string memory _riskLevel,
        string memory _modelVersion
    ) public {
        recordCount++;

        records[recordCount] = Record(
            recordCount,
            _userId,
            _predictionHash,
            _riskLevel,
            _modelVersion,
            block.timestamp
        );

        emit RecordStored(
            recordCount,
            _userId,
            _predictionHash,
            _riskLevel,
            _modelVersion,
            block.timestamp
        );
    }

    function getRecord(uint256 _recordId)
        public
        view
        returns (
            uint256,
            string memory,
            string memory,
            string memory,
            string memory,
            uint256
        )
    {
        Record memory r = records[_recordId];
        return (
            r.recordId,
            r.userId,
            r.predictionHash,
            r.riskLevel,
            r.modelVersion,
            r.timestamp
        );
    }
}