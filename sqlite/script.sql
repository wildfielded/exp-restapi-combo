PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE 'Users'    (
                        'uid' VARCHAR(36) NOT NULL PRIMARY KEY,
                        'name' VARCHAR(1024) DEFAULT NULL,
                        'login' VARCHAR(1024) DEFAULT NULL,
                        'password' VARCHAR(1024) DEFAULT NULL,
                        'acc_token' VARCHAR(1024) DEFAULT NULL,
                        'acc_expired' REAL DEFAULT NULL,
                        'ref_token' VARCHAR(1024) DEFAULT NULL,
                        'ref_expired' REAL DEFAULT NULL,
                        'comment' TEXT(1024) DEFAULT NULL
                        );
INSERT INTO 'Users' VALUES('00000000-1111-1111-1111-000000000000','James','user1','qwerty1',NULL,NULL,NULL,NULL,NULL);
INSERT INTO 'Users' VALUES('00000000-2222-2222-2222-000000000000','Jonny','user2','qwerty2',NULL,NULL,NULL,NULL,NULL);
INSERT INTO 'Users' VALUES('00000000-3333-3333-3333-000000000000','Jowie','user3','qwerty3',NULL,NULL,NULL,NULL,NULL);
COMMIT;
