CREATE TABLE companies
(
companiesId	INTEGER,
companiesName VARCHAR(70),
companiesDateCreated VARCHAR(70),	
createdBy VARCHAR(70),
companiesEmails	VARCHAR(70),
companiesPhones	VARCHAR(70),
employeesId	INTEGER,
employeesName VARCHAR(70),
usersResponsible VARCHAR(70),
sectorKey INTEGER
);
CREATE TABLE contacts 
(
    contactsId INTEGER,
    contactsName VARCHAR(70),
    contactsDateCreated	VARCHAR(70),
    contactsCreatedBy VARCHAR(70),
    contactsEmails	VARCHAR(70),
    contactsPhones	VARCHAR(70),
    contactsEmployers VARCHAR(70),
    employersId	INTEGER,
    contactsHomeAdress VARCHAR(70),
    contactsLatLong	VARCHAR(70),
    contactsRelatedToLead VARCHAR(70),
    contactsResponsible VARCHAR(70)
);
CREATE TABLE deals
(
    dealsId	INTEGER,
    dealsDateCreated VARCHAR(70),
    dealsPrice INTEGER,
    contactsId	INTEGER,
    companiesId INTEGER
);
CREATE TABLE sectors
(   
    sectorKey INTEGER,
    sector VARCHAR(70)
    
);
