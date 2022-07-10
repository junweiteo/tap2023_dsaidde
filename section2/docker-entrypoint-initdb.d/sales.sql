CREATE TABLE Sale (
    SalesID int NOT NULL,
    CarID int NOT NULL,
    TransDatetime TIMESTAMP NOT NULL,
    CustName VARCHAR NOT NULL,
    CustPhone VARCHAR NOT NULL,
    SalesPerson VARCHAR NOT NULL,
    PRIMARY KEY (SalesID),
    FOREIGN KEY (CarID) REFERENCES Car(CarID)
);
