SQLite format 3   @                                                                     .O}M L �pL                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        �<�OtableAutoridAutoridCREATE TABLE Autorid (
            autor_id INTEGER PRIMARY KEY AUTOINCREMENT,
            autor_nimi TEXT NOT NULL,
            sunnikuupaev DATE NOT NULL
    )�b�tableRaamatudRaamatudCREATE TABLE Raamatud (
        raamat_id INTEGER PRIMARY KEY AUTOINCREMENT,
        pealkiri TEXT NOT NULL,
        valjaandmise_kuupaev DATE NOT NULL,
        autor_id INTEGER,
        Zanr_id INTEGER,
        FOREIGN KEY(autor_id) REFERENCES Autorid(autor_id),
        FOREIGN KEY(Zanr_id) REFERENCES Zanrid(Zanr_id)
    )��ktableZanridZanridCREATE TABLE Zanrid (
        Zanr_id INTEGER PRIMARY KEY AUTOINCREMENT,
        Zanri_nimi TEXT NOT NULL
    )P++Ytablesqlite_sequencesqlite_sequenceCREATE TABLE sqlite_sequence(name,seq)   ��7tableAutoridAutoridCREATE TABLE Autorid (
        autor_id INTEGER PRIMARY KEY AUTOINCREMENT,
        autor_nimi TEXT NOT NULL,
        sunnikuupaev DATE NOT NU     � 	� ����cF%�                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         	 !Oskar1999-19-19 '!George Orwell1950-06-25 /!Bret Easton Ellis1964-02-03 '!George Orwell1950-06-25 /!Bret Easton Ellis1964-02-03 '!George Orwell1950-06-25 /!Bret Easton Ellis1964-02-03 '!George Orwell1950-06-25   /!Bret  !Peeter1999-10-10   � ���                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              AutoridAutorid	Raamatud
Zanrid    ������~hXB2                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               	 Horror /Political fiction #Dark Comedy
 /Political fiction	 #Dark Comedy /Political fiction #Dark Comedy /Political fiction #Dark Comedy /Political fiction #Dark Comedy /Political fiction #Dark Comedy� x ���wO0���`?����x                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           !	Kevad2000-10-10
 #!Animal Farm1945-08-17& 5!Nineteen Eighty-Four1949-02-07 +!		American Psycho1991-02-03 #!Animal Farm1945-08-17& 5!Nineteen Eighty-Four1949-02-07 +!		American Psycho1991-02-03 #!Animal Farm1945-08-17& 5!Nineteen Eighty-Four1949-02-07
 +!		American Psycho1991-02-03	 #!Animal Farm1945-08-17& 5!Nineteen Eighty-Four1949-02-07 +!		American Psycho1991-02-03 #!Animal Farm1945-08-17& 5!Nineteen Eighty-Four1949-02-07 +!		American Psycho1991-02-03 #!Animal Farm1945-08-17& 5!Nineteen Eighty-Four1949-02-07   +!		Ameri !		ee2000-12-12