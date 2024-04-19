import random

guests = [('Claudia Darker', 'Menino', 'EE VIRIATO BANDEIRA/COXIM'), ('Inger Lamborne', 'Menino', 'EE SEN FILINTO MULLER'), ('Fitz Tarte', 'Menino', 'IFMS - NAVIRAÍ'), ('Aime Whittlesey', 'Menina', 'IFMS - NOVA ANDRADINA'), ('Mareah Umbers', 'Menino', 'UFMS'), ("Chev O'Hollegan", 'Menino', 'UFMS-CPAN'), ('Phyllida Marte', 'Menina', 'EE PROF JOÃO MAGIANO PINTO - TRES LAGOAS'), ('Lyda Bontein', 'Menino', 'IFMS - NAVIRAÍ'), ('Noelle Hiscocks', 'Menina', 'IFMS - COXIM'), ('Sonnie Campany', 'Menino', 'EE Marechal Rondon / NOVA ANDRADINA'), ('Reggie Duckerin', 'Menino', 'VAGO'), ('Adriaens Gregori', 'Menina', 'EE MIN JOÃO PAULO DOS REIS VELOSO - DOURADOS'), ("Sonny O'Hearn", 'Menina', 'E PROF. JOSÉ JUAREZ R DE OLIVEIRA - ITAQUIRAÍ'), ('Bird Zannuto', 'Menina', 'EE MIN JOÃO PAULO DOS REIS VELOSO - DOURADOS'), ('Kalinda Beyer', 'Menina', 'EE MARIA DA GLORIA MUZZI FERREIRA - DOURADOS'), ('Clarance Stains', 'Menino', 'EE MIN JOÃO PAULO DOS REIS VELOSO - DOURADOS'), ('Terrill Sheber', 'Menino', 'IFMS - DOURADOS'), ('Tabor Brook', 'Menino', 'E.E. PROFª GENI MARQUES MAGALHÃES - PONTA PORÃ'), ('Taddeusz Dendon', 'Menina', 'E.E. JOSÉ GARCIA LEAL - PARANAIBA'), ('Trey De Roeck', 'Menino', 'EE MARIA DA GLORIA MUZZI FERREIRA - DOURADOS'), ('Ellswerth Beamand', 'Menino', 'VAGO'), ('Hinze Hickenbottom', 'Menino', 'EE VIRIATO BANDEIRA/COXIM'), ('Thatch Janeway', 'Menina', 'EE MIN JOÃO PAULO DOS REIS VELOSO - DOURADOS'), ('Gretal Bredee', 'Menino', 'EE REYNALDO MASSI/IVINHEMA'), ('Iormina Botting', 'Menino', 'EE FLORIANO VIEGAS MACHADO - DOURADOS'), ('Salomon Locard', 'Menino', 'VAGO'), ('Kienan Emslie', 'Menino', 'EE JULIA GONCALVES PASSARINHO - CORUMBA'), ('Adelina Beese', 'Menino', 'IFMS - COXIM'), ('Elset Lavery', 'Menino', 'EE PROFª GENI MARQUES MAGALHÃES - PONTA PORÃ'), ('Reinhold Fagence', 'Menina', 'EE MARIA DA GLORIA MUZZI FERREIRA - DOURADOS'), ('Delia Gibbons', 'Menino', 'IFMS - NOVA ANDRADINA'), ('Romola Kidston', 'Menino', 'IFMS - AQUIDAUANA'), ('Modesta Matskiv', 'Menino', 'IFMS - NAVIRAÍ'), ('Haywood Watkinson', 'Menino', 'E PROF. JOSÉ JUAREZ R DE OLIVEIRA - ITAQUIRAÍ'), ('Randolf Veronique', 'Menina', 'EE MARIA DA GLORIA MUZZI FERREIRA - DOURADOS'), ('Katleen Treadaway', 'Menino', 'EE VIRIATO BANDEIRA - COXIM'), ('Moyra Castiglione', 'Menina', 'EE Marechal Rondon / NOVA ANDRADINA'), ('Berkly Densham', 'Menino', 'IFMS - NOVA ANDRADINA'), ('Alma Garnham', 'Menina', 'EE INDIGENA CACIQUE TIMOTEO - MIRANDA'), ('Marisa Eversley', 'Menina', 'FETEC'), ('Marne Seywood', 'Menino', 'EE CEL JOSÉ ALVES RIBEIRO - AQUIDAUANA'), ('Gerry Bollin', 'Menino', 'EE SEN FILINTO MULLER/IVINHEMA'), ('Georgena Maxwale', 'Menino', 'EE PROFª GENI MARQUES MAGALHÃES - PONTA PORÃ'), ('Hallsy Cuningham', 'Menina', 'EE PRES VARGAS - DOURADOS'), ('Elwood Huster', 'Menina', 'IFMS - COXIM'), ('Donnie McFayden', 'Menino', 'EE MARIA DA GLORIA MUZZI FERREIRA - DOURADOS'), ('Paul Plues', 'Menina', 'EE VIRIATO BANDEIRA/COXIM'), ('Philippa Forbes', 'Menina', 'EE MARIA DA GLORIA MUZZI FERREIRA - DOURADOS'), ('Mathe Godfrey', 'Menino', 'IFMS - PONTA PORÃ'), ('Thurstan Saunders', 'Menina', 'EE VIRIATO BANDEIRA/COXIM'), ('Karla Filpi', 'Menina', 'EE SEN FILINTO MULLER/IVINHEMA'), ('Etty Gartell', 'Menino', 'EE MARIA DA GLORIA MUZZI FERREIRA - DOURADOS'), ('Vitia Cassell', 'Menina', 'IFMS - NOVA ANDRADINA'), ('Urbain Granger', 'Menina', 'UFMS-CPTL'), ('Bekki Cocks', 'Menina', 'EE VIRIATO BANDEIRA - COXIM'), ('Niko Davydzenko', 'Menina', 'EE INDIGENA CACIQUE TIMOTEO - MIRANDA'), ('Ryon Hunter', 'Menino', 'IFMS - COXIM'), ('Rosmunda Sellors', 'Menino', 'EE ADE MARQUES - PONTA PORÃ'), ('Ogdon Folk', 'Menina', 'EE PROFESSOR JOSÉ PEREIRA LINS - DOURADOS'), ('Caryn Shier', 'Menino', 'EE VIRIATO BANDEIRA - COXIM'), ('Charla Willoway', 'Menino', 'EE REYNALDO MASSI/IVINHEMA'), ('Lela Maffioni', 'Menino', 'E PROF. JOSÉ JUAREZ R DE OLIVEIRA - ITAQUIRAÍ'), ('Land McGannon', 'Menino', 'FETEC'), ('Far Barkas', 'Menina', 'EE VIRIATO BANDEIRA/COXIM'), ('Sophey Congram', 'Menino', 'VAGO'), ('Cindie Eastwell', 'Menino', 'EE PROFESSOR JOSÉ PEREIRA LINS - DOURADOS'), ('Lynn Fludgate', 'Menina', 'VAGO'), ('Candide Crates', 'Menino', 'FETEC'), ('Casandra Abrahamowitcz', 'Menino', 'UFMS'), ('Kaia Knapton', 'Menino', 'EE PROF JOÃO MAGIANO PINTO - TRES LAGOAS'), ('Charlotta Cussen', 'Menino', 'EE CEL JOSÉ ALVES RIBEIRO - AQUIDAUANA'), ('Adolph Cisec', 'Menina', 'EE INDIGENA CACIQUE TIMÓTEO - MIRANDA'), ("Angelico O'Downe", 'Menino', 'EE PROFª GENI MARQUES MAGALHÃES - PONTA PORÃ'), ('Morie Elflain', 'Menino', 'EE REYNALDO MASSI/IVINHEMA'), ('Charline Dowdney', 'Menina', 'EE REYNALDO MASSI/IVINHEMA'), ('Anthony Kornas', 'Menina', 'EE INDIGENA CACIQUE TIMÓTEO - MIRANDA'), ('Orel Barhems', 'Menina', 'VAGO'), ('Shandy Leftwich', 'Menino', 'EE REYNALDO MASSI/IVINHEMA'), ('Boyce Darwen', 'Menina', 'UFMS-CPTL'), ('Sandra Tumber', 'Menina', 'IFMS - PONTA PORÃ'), ('Stacy Rimer', 'Menina', 'EE INDIGENA CACIQUE TIMOTEO - MIRANDA'), ('Tildi Turrill', 'Menina', 'UFMS'), ('Philomena Placstone', 'Menina', 'E PROF. JOSÉ JUAREZ R DE OLIVEIRA - ITAQUIRAÍ'), ('Chrissie Pidgeon', 'Menino', 'EE FLORIANO VIEGAS MACHADO - DOURADOS'), ('Karna Malcolmson', 'Menino', 'UFMS-CPTL'), ('Thatcher Klempke', 'Menino', 'E.E. JOSÉ GARCIA LEAL - PARANAIBA'), ('Caddric Mc Carrick', 'Menino', 'EE FLORIANO VIEGAS MACHADO - DOURADOS'), ('Rudy Pischel', 'Menina', 'FETEC'), ('Mahmud Rycroft', 'Menina', 'FETEC'), ('Mellie Carrett', 'Menina', 'UFMS-CPTL'), ('Phillipe Tumelty', 'Menina', 'EE MARIA DA GLORIA MUZZI FERREIRA - DOURADOS'), ('Mamie Grigoryev', 'Menino', 'EE PROFESSOR JOSÉ PEREIRA LINS - DOURADOS'), ('Zarah Davys', 'Menino', 'EE JULIA GONCALVES PASSARINHO - CORUMBA'), ('Verile Pietruszka', 'Menina', 'EE VIRIATO BANDEIRA - COXIM'), ('Lark Romagosa', 'Menina', 'IFMS - AQUIDAUANA'), ('Asia Basey', 'Menina', 'EE SEN FILINTO MULLER/IVINHEMA'), ('Nikkie Lukes', 'Menina', 'E.E. PROFª GENI MARQUES MAGALHÃES - PONTA PORÃ'), ('Lorry Castagne', 'Menino', 'IFMS - COXIM'), ('Kristos Crumly', 'Menino', 'IFMS - DOURADOS'), ('Almire Wozencraft', 'Menino', 'EE FLORIANO VIEGAS MACHADO - DOURADOS'), ('Eveline Andersen', 'Menina', 'IFMS - NOVA ANDRADINA'), ('Leah Tow', 'Menino', 'EE Marechal Rondon / NOVA ANDRADINA'), ('Gayler Thomasson', 'Menina', 'IFMS - NOVA ANDRADINA'), ('Kassey Venediktov', 'Menino', 'EE SEN FILINTO MULLER/IVINHEMA'), ('Carrie Grayer', 'Menino', 'EE INDIGENA CACIQUE TIMÓTEO - MIRANDA'), ('Bartholemy Camplejohn', 'Menino', 'EE SEN FILINTO MULLER'), ('Natal Garner', 'Menino', 'FETEC'), ('Norman Gingell', 'Menino', 'EE FLORIANO VIEGAS MACHADO - DOURADOS'), ('Damien Divisek', 'Menina', 'E.E. PROFª GENI MARQUES MAGALHÃES - PONTA PORÃ'), ('Archie Doumerc', 'Menino', 'EE MIN JOÃO PAULO DOS REIS VELOSO - DOURADOS'), ('Bel Ogelbe', 'Menino', 'EE REYNALDO MASSI/IVINHEMA'), ('Dido Husset', 'Menina', 'EE PROFª GENI MARQUES MAGALHÃES - PONTA PORÃ'), ('Roderic Kilgrove', 'Menina', 'UFMS-CPTL'), ('Miguel Bathersby', 'Menina', 'EE VIRIATO BANDEIRA/COXIM'), ('Aviva Lanaway', 'Menino', 'EE PROF JOÃO MAGIANO PINTO - TRES LAGOAS'), ('Feliks Ourtic', 'Menina', 'EE VIRIATO BANDEIRA/COXIM'), ('Irwin Stowell', 'Menina', 'EE INDIGENA CACIQUE TIMÓTEO - MIRANDA'), ('Georgianna Holywell', 'Menina', 'EE INDIGENA CACIQUE TIMOTEO - MIRANDA'), ('Agustin Ellerbeck', 'Menino', 'EE PROF JOÃO MAGIANO PINTO - TRES LAGOAS'), ('Irena Titchmarsh', 'Menino', 'EE DOM BOSCO - CORUMBA'), ('Dagny Danit', 'Menina', 'E.E. JOSÉ GARCIA LEAL - PARANAIBA'), ('Remy Hanscomb', 'Menina', 'EE MARIA DA GLORIA MUZZI FERREIRA - DOURADOS'), ('Becky Starie', 'Menino', 'IFMS - DOURADOS'), ('Ebba McNeachtain', 'Menino', 'EE Marechal Rondon / NOVA ANDRADINA'), ('Lefty Mac Giolla Pheadair', 'Menino', 'IFMS - PONTA PORÃ'), ('Linzy Leiden', 'Menina', 'EE VIRIATO BANDEIRA/COXIM'), ('Blakelee Bakeup', 'Menina', 'UFMS'), ('Lorette Dunster', 'Menina', 'IFMS - PONTA PORÃ'), ('Jennilee Heindl', 'Menina', 'UFMS-CPAN'), ('Herculie Tarzey', 'Menino', 'IFMS - PONTA PORÃ'), ('Ramsey Wingham', 'Menino', 'EE INDIGENA CACIQUE TIMÓTEO - MIRANDA'), ('Guss Barca', 'Menina', 'EE INDIGENA CACIQUE TIMÓTEO - MIRANDA'), ('Megan Cubberley', 'Menina', 'EE PROF JOÃO MAGIANO PINTO - TRES LAGOAS'), ('Chris Bennion', 'Menino', 'IFMS - DOURADOS'), ('Florida Keepin', 'Menino', 'EE ADE MARQUES - PONTA PORÃ'), ('Grissel Maffy', 'Menino', 'IFMS - DOURADOS'), ('Tiler Machan', 'Menina', 'IFMS - NAVIRAÍ'), ('Maddy Farriar', 'Menina', 'E.E. JOSÉ GARCIA LEAL - PARANAIBA'), ('Hamlin Ilive', 'Menina', 'E PROF. JOSÉ JUAREZ R DE OLIVEIRA - ITAQUIRAÍ'), ('Marci Pepler', 'Menina', 'EE Marechal Rondon / NOVA ANDRADINA'), ('Shandee Atmore', 'Menino', 'UFMS-CPTL'), ('Storm Fiddyment', 'Menina', 'IFMS - NOVA ANDRADINA'), ('Crichton Kneale', 'Menino', 'EE PROFª GENI MARQUES MAGALHÃES - PONTA PORÃ'), ('Justis Brasse', 'Menino', 'EE INDIGENA CACIQUE TIMÓTEO - MIRANDA'), ('Margette McIndoe', 'Menino', 'EE MARIA DA GLORIA MUZZI FERREIRA - DOURADOS'), ('Monty Cristol', 'Menino', 'EE REYNALDO MASSI/IVINHEMA'), ('Jerrold Jollie', 'Menino', 'EE MIN JOÃO PAULO DOS REIS VELOSO - DOURADOS'), ('Meryl Womack', 'Menino', 'EE CEL JOSÉ ALVES RIBEIRO - AQUIDAUANA'), ('Justinian Alabaster', 'Menina', 'EE INDIGENA CACIQUE TIMÓTEO - MIRANDA'), ('Ethelyn Chaffey', 'Menino', 'FETEC'), ('Neall Peoples', 'Menino', 'EE PROF JOÃO MAGIANO PINTO - TRES LAGOAS'), ('Dael Pankhurst.', 'Menino', 'EE MIN JOÃO PAULO DOS REIS VELOSO - DOURADOS'), ('Jon Dinnage', 'Menino', 'EE INDIGENA CACIQUE TIMOTEO - MIRANDA'), ('Farris Daleman', 'Menino', 'EE FLORIANO VIEGAS MACHADO - DOURADOS'), ('Chrissie Klaas', 'Menino', 'E PROF. JOSÉ JUAREZ R DE OLIVEIRA - ITAQUIRAÍ'), ('Elwira Truin', 'Menino', 'UFMS-CPTL'), ('Raina Swede', 'Menino', 'IFMS - AQUIDAUANA'), ('Hyacinthie Isaksson', 'Menina', 'EE PROFª GENI MARQUES MAGALHÃES - PONTA PORÃ'), ("Bentley O'Lenane", 'Menina', 'IFMS - DOURADOS'), ('Madelin Trevna', 'Menina', 'IFMS - COXIM'), ('Hailee Mixter', 'Menino', 'EE INDIGENA CACIQUE TIMOTEO - MIRANDA'), ('Ring Walewicz', 'Menina', 'EE MIN JOÃO PAULO DOS REIS VELOSO - DOURADOS'), ('Sheelagh Slarke', 'Menina', 'E.E. JOSÉ GARCIA LEAL - PARANAIBA'), ('Oby Scrancher', 'Menina', 'EE CEL JOSÉ ALVES RIBEIRO - AQUIDAUANA'), ('Perla Gallant', 'Menino', 'VAGO'), ('Samuele Loache', 'Menina', 'IFMS - NOVA ANDRADINA'), ('Giustino Loughan', 'Menino', 'EE MIN JOÃO PAULO DOS REIS VELOSO - DOURADOS'), ('Troy Linthead', 'Menino', 'IFMS - NOVA ANDRADINA'), ('Lucila Jirick', 'Menina', 'EE PROF JOÃO MAGIANO PINTO - TRES LAGOAS'), ('Abbey Croasdale', 'Menina', 'FETEC'), ('Yelena Beardsdale', 'Menino', 'EE VIRIATO BANDEIRA - COXIM'), ('Valle Lowdyane', 'Menina', 'EE INDIGENA CACIQUE TIMOTEO - MIRANDA'), ('Livia Hadkins', 'Menino', 'IFMS - DOURADOS'), ('Penni Gatland', 'Menina', 'FETEC'), ('Tedd Goulbourn', 'Menino', 'EE INDIGENA CACIQUE TIMOTEO - MIRANDA'), ('Herman Ruthven', 'Menina', 'E PROF. JOSÉ JUAREZ R DE OLIVEIRA - ITAQUIRAÍ'), ('Claire Knoton', 'Menino', 'EE PRES VARGAS - DOURADOS'), ('Stormi Jervis', 'Menino', 'UFMS'), ('Nevile Van Der Straaten', 'Menina', 'IFMS - AQUIDAUANA'), ('Biddy Cullotey', 'Menina', 'EE PROFESSOR JOSÉ PEREIRA LINS - DOURADOS'), ('Nonie Coudray', 'Menino', 'UFMS-CPTL'), ('Brena Dyte', 'Menina', 'EE MARIA DA GLORIA MUZZI FERREIRA - DOURADOS'), ('Marigold Meale', 'Menina', 'EE ADE MARQUES - PONTA PORÃ'), ('Sabine Lacotte', 'Menino', 'IFMS - NAVIRAÍ'), ('Merl Headley', 'Menina', 'EE Marechal Rondon / NOVA ANDRADINA'), ('Roarke Cutchey', 'Menina', 'IFMS - AQUIDAUANA'), ('Carr Farnish', 'Menino', 'EE MARIA DA GLORIA MUZZI FERREIRA - DOURADOS'), ('Georgeanne Bartoletti', 'Menino', 'EE PROFª GENI MARQUES MAGALHÃES - PONTA PORÃ'), ('Karoly Chrichton', 'Menina', 'EE PROFª GENI MARQUES MAGALHÃES - PONTA PORÃ'), ('Rosita Edghinn', 'Menina', 'EE MARIA DA GLORIA MUZZI FERREIRA - DOURADOS'), ('Merrill Loody', 'Menina', 'FETEC'), ('Sallee Stelli', 'Menino', 'FETEC'), ('Woodman Robertazzi', 'Menino', 'IFMS - NOVA ANDRADINA'), ('Debor Gauntlett', 'Menino', 'EE REYNALDO MASSI/IVINHEMA'), ('Terza Gobel', 'Menino', 'FETEC'), ('Eran Calderhead', 'Menino', 'EE FLORIANO VIEGAS MACHADO - DOURADOS'), ('Paulina Josef', 'Menina', 'E.E. PROFª GENI MARQUES MAGALHÃES - PONTA PORÃ'), ('Khalil Leal', 'Menina', 'E PROF. JOSÉ JUAREZ R DE OLIVEIRA - ITAQUIRAÍ'), ('Keven Zecchinii', 'Menina', 'UFMS'), ('Sallee Thornbarrow', 'Menina', 'EE PROF JOÃO MAGIANO PINTO - TRES LAGOAS'), ('Margalo Barbera', 'Menino', 'E.E. JOSÉ GARCIA LEAL - PARANAIBA'), ('Meaghan Vickerstaff', 'Menina', 'EE SEN FILINTO MULLER'), ('Indira Fargher', 'Menino', 'UFMS-CPAN'), ('Sophi Gowlett', 'Menino', 'EE PRES VARGAS - DOURADOS'), ('Ola Tinline', 'Menino', 'FETEC'), ('Chad Greenleaf', 'Menina', 'EE JULIA GONCALVES PASSARINHO - CORUMBA'), ('Rhetta Jeskin', 'Menino', 'IFMS - COXIM'), ('Marcel Izsak', 'Menino', 'IFMS - NAVIRAÍ'), ('Charmane Tatlowe', 'Menina', 'EE MARIA DA GLORIA MUZZI FERREIRA - DOURADOS'), ('Rollie Tomkys', 'Menina', 'IFMS - NOVA ANDRADINA'), ('Jeffrey Featherstonhaugh', 'Menino', 'EE SEN FILINTO MULLER/IVINHEMA'), ('Luciano Izard', 'Menina', 'EE CEL JOSÉ ALVES RIBEIRO - AQUIDAUANA'), ('Darya Branch', 'Menino', 'EE MARIA DA GLORIA MUZZI FERREIRA - DOURADOS'), ('Charmain Lomansey', 'Menina', 'IFMS - DOURADOS'), ('Joly Chevins', 'Menino', 'IFMS - COXIM'), ('Chickie Sycamore', 'Menino', 'EE PRES VARGAS - DOURADOS'), ('Baily Cuttler', 'Menina', 'EE REYNALDO MASSI/IVINHEMA'), ('Ingar Haines', 'Menina', 'EE MIN JOÃO PAULO DOS REIS VELOSO - DOURADOS'), ('Nannette Fyfe', 'Menino', 'UFMS-CPAN'), ('Remy Fulle', 'Menino', 'FETEC'), ('Stu Lochhead', 'Menina', 'UFMS-CPAN'), ('Jarib Archer', 'Menina', 'EE PROFESSOR JOSÉ PEREIRA LINS - DOURADOS'), ('Wilt Lowthian', 'Menino', 'EE PRES VARGAS - DOURADOS'), ('Gypsy Tarborn', 'Menino', 'IFMS - NAVIRAÍ'), ('Nickie Fairclough', 'Menino', 'UFMS'), ('Sandi Kopisch', 'Menina', 'EE MIN JOÃO PAULO DOS REIS VELOSO - DOURADOS'), ('Patrizius Fasey', 'Menina', 'EE MARIA DA GLORIA MUZZI FERREIRA - DOURADOS'), ('Gweneth Sawdy', 'Menina', 'EE PRES VARGAS - DOURADOS'), ('Katey Vakhlov', 'Menina', 'EE JULIA GONCALVES PASSARINHO - CORUMBA'), ('Chic Scoble', 'Menina', 'FETEC'), ('Pip Base', 'Menino', 'EE PROF JOÃO MAGIANO PINTO - TRES LAGOAS'), ('Dixie Bale', 'Menina', 'E.E. JOSÉ GARCIA LEAL - PARANAIBA'), ('Bernadine Cappleman', 'Menino', 'EE ADE MARQUES - PONTA PORÃ'), ('Romy Vauter', 'Menino', 'FETEC'), ('Arnaldo Muncaster', 'Menina', 'EE PROF JOÃO MAGIANO PINTO - TRES LAGOAS'), ('Vinni Chettle', 'Menina', 'EE VIRIATO BANDEIRA - COXIM'), ('Morena Belsham', 'Menino', 'IFMS - PONTA PORÃ'), ('Tamiko Baglin', 'Menina', 'UFMS-CPAN'), ('Octavia Eck', 'Menino', 'IFMS - NAVIRAÍ'), ('Eldridge Monard', 'Menino', 'EE CEL JOSÉ ALVES RIBEIRO - AQUIDAUANA'), ('Herbie Nicklin', 'Menina', 'IFMS - COXIM'), ('Gallagher Renak', 'Menina', 'EE REYNALDO MASSI/IVINHEMA'), ('Augustina Unitt', 'Menina', 'EE INDIGENA CACIQUE TIMOTEO - MIRANDA'), ('Evy Flipek', 'Menino', 'EE FLORIANO VIEGAS MACHADO - DOURADOS'), ('Kerianne Eastlake', 'Menina', 'EE INDIGENA CACIQUE TIMÓTEO - MIRANDA'), ('Ericha Snoxall', 'Menina', 'UFMS-CPAN'), ('Dorene Scard', 'Menino', 'FETEC'), ('Martino Beals', 'Menina', 'IFMS - COXIM'), ('Yance Lorie', 'Menina', 'EE VIRIATO BANDEIRA - COXIM'), ('Jo Szabo', 'Menina', 'UFMS'), ('Isa Ivanilov', 'Menino', 'UFMS-CPTL'), ('Lonni Mudie', 'Menina', 'EE SEN FILINTO MULLER/IVINHEMA'), ('Dannie Collens', 'Menina', 'UFMS-CPTL'), ('Dahlia Zimmermanns', 'Menina', 'EE PROFª GENI MARQUES MAGALHÃES - PONTA PORÃ'), ('Dorita Rathmell', 'Menina', 'EE SEN FILINTO MULLER'), ('Flori Goodey', 'Menina', 'FETEC'), ('Norbert Petrashov', 'Menino', 'IFMS - NAVIRAÍ'), ('Thekla Estcourt', 'Menino', 'EE MIN JOÃO PAULO DOS REIS VELOSO - DOURADOS'), ('Iosep Alway', 'Menina', 'EE MIN JOÃO PAULO DOS REIS VELOSO - DOURADOS'), ('Peggi Alessandrini', 'Menino', 'EE PROFª GENI MARQUES MAGALHÃES - PONTA PORÃ'), ('Zorina Jaszczak', 'Menina', 'EE PROFESSOR JOSÉ PEREIRA LINS - DOURADOS'), ('Jo-ann Collings', 'Menina', 'UFMS'), ('Wallie Zannelli', 'Menina', 'EE ADE MARQUES - PONTA PORÃ'), ('Hewe Bettison', 'Menino', 'FETEC'), ('Domini Titley', 'Menina', 'IFMS - AQUIDAUANA'), ('Noel Jacobowitz', 'Menina', 'IFMS - NAVIRAÍ'), ('Hannah Chaplain', 'Menino', 'UFMS-CPTL'), ('Stillman Andersson', 'Menina', 'UFMS-CPAN'), ('Marshall Bachelar', 'Menina', 'FETEC'), ('Jozef Oret', 'Menino', 'EE SEN FILINTO MULLER'), ('Neville Raikes', 'Menina', 'EE CEL JOSÉ ALVES RIBEIRO - AQUIDAUANA'), ('Phylis Baty', 'Menino', 'EE Marechal Rondon / NOVA ANDRADINA'), ('Wolf Hourston', 'Menina', 'EE Marechal Rondon / NOVA ANDRADINA'), ('Felic Sworne', 'Menina', 'VAGO'), ('Dode Allanby', 'Menina', 'UFMS-CPTL'), ('Cleavland Cann', 'Menina', 'VAGO'), ('Robenia Crayden', 'Menino', 'EE SEN FILINTO MULLER'), ('Rriocard Whichelow', 'Menina', 'EE CEL JOSÉ ALVES RIBEIRO - AQUIDAUANA'), ('Melinda Spoor', 'Menina', 'EE SEN FILINTO MULLER'), ('Glendon Hanlon', 'Menino', 'EE Marechal Rondon / NOVA ANDRADINA'), ('Toni Oldam', 'Menino', 'IFMS - COXIM'), ('Powell Oven', 'Menino', 'IFMS - NAVIRAÍ'), ('Tallulah Knappett', 'Menino', 'EE Marechal Rondon / NOVA ANDRADINA'), ('Donny Laurance', 'Menina', 'EE REYNALDO MASSI/IVINHEMA'), ('Valera Castiglione', 'Menino', 'EE INDIGENA CACIQUE TIMÓTEO - MIRANDA'), ('Janene Warboy', 'Menina', 'EE SEN FILINTO MULLER/IVINHEMA'), ('Tamarah Decayette', 'Menina', 'E.E. JOSÉ GARCIA LEAL - PARANAIBA'), ('Danielle Order', 'Menino', 'EE SEN FILINTO MULLER/IVINHEMA'), ('Harris Nowill', 'Menino', 'E.E. JOSÉ GARCIA LEAL - PARANAIBA'), ('Mariette Delacourt', 'Menina', 'EE MARIA DA GLORIA MUZZI FERREIRA - DOURADOS'), ('Cherlyn Olland', 'Menino', 'UFMS'), ('Augie Fitzsimmons', 'Menino', 'EE INDIGENA CACIQUE TIMÓTEO - MIRANDA'), ('Yovonnda Chandlar', 'Menina', 'EE DOM BOSCO - CORUMBA'), ('Edouard Sandford', 'Menino', 'EE VIRIATO BANDEIRA/COXIM'), ('Sofia Mixture', 'Menino', 'EE CEL JOSÉ ALVES RIBEIRO - AQUIDAUANA'), ('Micheline Bewlie', 'Menina', 'E.E. PROFª GENI MARQUES MAGALHÃES - PONTA PORÃ'), ('Marsha Levinge', 'Menina', 'IFMS - DOURADOS'), ('Crysta Blindermann', 'Menino', 'EE ADE MARQUES - PONTA PORÃ'), ('Griff Itzkovsky', 'Menina', 'IFMS - NOVA ANDRADINA'), ('Claudio Scarfe', 'Menino', 'EE VIRIATO BANDEIRA - COXIM'), ('Candy McClymont', 'Menina', 'EE INDIGENA CACIQUE TIMÓTEO - MIRANDA'), ('Welbie Arthy', 'Menina', 'EE CEL JOSÉ ALVES RIBEIRO - AQUIDAUANA'), ('Reuven Reinbech', 'Menino', 'IFMS - AQUIDAUANA'), ('Cristy Sennett', 'Menino', 'UFMS-CPTL'), ('Fulton Baumber', 'Menina', 'IFMS - NAVIRAÍ'), ('Rosita Kesteven', 'Menina', 'EE FLORIANO VIEGAS MACHADO - DOURADOS'), ('Reba Prickett', 'Menina', 'IFMS - NOVA ANDRADINA'), ('Zacharie Boeter', 'Menino', 'EE CEL JOSÉ ALVES RIBEIRO - AQUIDAUANA'), ('Syman Scrowby', 'Menina', 'EE Marechal Rondon / NOVA ANDRADINA'), ('Idaline Kimmitt', 'Menina', 'UFMS-CPTL'), ('Karon Currier', 'Menina', 'EE SEN FILINTO MULLER'), ('Karia Dodle', 'Menino', 'IFMS - DOURADOS'), ('Deanne Prattin', 'Menina', 'E.E. PROFª GENI MARQUES MAGALHÃES - PONTA PORÃ'), ('Claresta Stopford', 'Menina', 'EE MARIA DA GLORIA MUZZI FERREIRA - DOURADOS'), ('Mersey Wakeling', 'Menina', 'UFMS-CPAN'), ('Ara Crosskell', 'Menino', 'E.E. JOSÉ GARCIA LEAL - PARANAIBA'), ('Rudolf Mazzey', 'Menina', 'EE PROF JOÃO MAGIANO PINTO - TRES LAGOAS'), ('Vidovic Rimmington', 'Menina', 'EE JULIA GONCALVES PASSARINHO - CORUMBA'), ('Willi Keitley', 'Menina', 'UFMS'), ('Alexi Ilyushkin', 'Menina', 'E PROF. JOSÉ JUAREZ R DE OLIVEIRA - ITAQUIRAÍ'), ('Zedekiah Twede', 'Menino', 'EE VIRIATO BANDEIRA - COXIM'), ('Rene Hanster', 'Menina', 'EE SEN FILINTO MULLER/IVINHEMA'), ('Sid Horbart', 'Menino', 'EE VIRIATO BANDEIRA/COXIM'), ('Marsha McEntagart', 'Menina', 'EE INDIGENA CACIQUE TIMÓTEO - MIRANDA'), ('Melisenda Paske', 'Menina', 'IFMS - DOURADOS'), ('Guillaume Yuille', 'Menina', 'UFMS-CPAN'), ('Dionysus Oulet', 'Menino', 'EE INDIGENA CACIQUE TIMÓTEO - MIRANDA'), ('Adela Bentall', 'Menino', 'EE INDIGENA CACIQUE TIMÓTEO - MIRANDA'), ('Hyacinthia Drexel', 'Menina', 'EE SEN FILINTO MULLER'), ('Malissa Vasyunkin', 'Menina', 'EE INDIGENA CACIQUE TIMOTEO - MIRANDA'), ('Willow Pullan', 'Menina', 'EE CEL JOSÉ ALVES RIBEIRO - AQUIDAUANA'), ('Robby Shalcros', 'Menina', 'EE INDIGENA CACIQUE TIMÓTEO - MIRANDA'), ('Cathy Worling', 'Menino', 'UFMS'), ('Jolynn Whodcoat', 'Menino', 'EE Marechal Rondon / NOVA ANDRADINA'), ('Roseann Tollfree', 'Menina', 'UFMS'), ('Noll Wardall', 'Menina', 'IFMS - AQUIDAUANA'), ('Shaine Webben', 'Menina', 'EE INDIGENA CACIQUE TIMOTEO - MIRANDA'), ('Pooh Cathersides', 'Menino', 'IFMS - NAVIRAÍ'), ('Coleman Foottit', 'Menino', 'EE DOM BOSCO - CORUMBA'), ('Wren Normanell', 'Menino', 'EE MIN JOÃO PAULO DOS REIS VELOSO - DOURADOS'), ('Donnie Roycraft', 'Menina', 'EE ADE MARQUES - PONTA PORÃ'), ('Aleen Jordan', 'Menino', 'EE CEL JOSÉ ALVES RIBEIRO - AQUIDAUANA'), ('Malvina Meehan', 'Menino', 'EE DOM BOSCO - CORUMBA'), ('Beryl Acutt', 'Menino', 'IFMS - DOURADOS'), ('Bourke Olivi', 'Menino', 'EE SEN FILINTO MULLER/IVINHEMA'), ('Eugen Hartropp', 'Menina', 'EE INDIGENA CACIQUE TIMÓTEO - MIRANDA'), ('Dermot Gaythor', 'Menino', 'EE VIRIATO BANDEIRA/COXIM'), ('Celestyn Penkman', 'Menina', 'EE PROFESSOR JOSÉ PEREIRA LINS - DOURADOS'), ('Romeo Zollner', 'Menino', 'EE INDIGENA CACIQUE TIMOTEO - MIRANDA'), ('Noellyn Watmore', 'Menina', 'EE MIN JOÃO PAULO DOS REIS VELOSO - DOURADOS'), ('Kent Blaxeland', 'Menina', 'IFMS - COXIM'), ('Nealon Gormally', 'Menino', 'EE MARIA DA GLORIA MUZZI FERREIRA - DOURADOS'), ('Gabbie Rogger', 'Menino', 'EE FLORIANO VIEGAS MACHADO - DOURADOS'), ('Noni Brecher', 'Menina', 'IFMS - AQUIDAUANA'), ('Hagan Bocock', 'Menina', 'IFMS - COXIM'), ('Dione Bemlott', 'Menina', 'EE PROF JOÃO MAGIANO PINTO - TRES LAGOAS'), ('Luciana Pasfield', 'Menino', 'EE DOM BOSCO - CORUMBA'), ('Chandler Jakubovits', 'Menina', 'EE INDIGENA CACIQUE TIMÓTEO - MIRANDA'), ('Nichole Bryden', 'Menino', 'VAGO'), ('Kirby Tirrey', 'Menino', 'E.E. JOSÉ GARCIA LEAL - PARANAIBA'), ("Celine O'Mullally", 'Menino', 'E.E. JOSÉ GARCIA LEAL - PARANAIBA'), ('Alverta Dregan', 'Menina', 'EE INDIGENA CACIQUE TIMOTEO - MIRANDA'), ('Odelia Davidman', 'Menina', 'EE FLORIANO VIEGAS MACHADO - DOURADOS'), ('Shaylynn Guitonneau', 'Menino', 'E PROF. JOSÉ JUAREZ R DE OLIVEIRA - ITAQUIRAÍ'), ('Sylvia Dutnall', 'Menina', 'UFMS-CPAN'), ('Horatia Sponer', 'Menina', 'EE PRES VARGAS - DOURADOS'), ('Teriann Purcer', 'Menino', 'EE DOM BOSCO - CORUMBA'), ('Antonetta Nornable', 'Menina', 'EE PROFESSOR JOSÉ PEREIRA LINS - DOURADOS'), ('Fenelia Dene', 'Menina', 'IFMS - DOURADOS'), ('Dita Bartlomieczak', 'Menino', 'EE JULIA GONCALVES PASSARINHO - CORUMBA'), ('Berne Brooks', 'Menino', 'IFMS - PONTA PORÃ'), ('Hamish Iorns', 'Menina', 'EE PRES VARGAS - DOURADOS'), ('Phyllys Fernando', 'Menino', 'EE MIN JOÃO PAULO DOS REIS VELOSO - DOURADOS'), ('Halley Manske', 'Menina', 'UFMS'), ('Beatrix Rugieri', 'Menino', 'UFMS-CPTL'), ('Marys Dinnage', 'Menina', 'IFMS - NAVIRAÍ'), ('Korey Corsham', 'Menino', 'IFMS - NAVIRAÍ'), ('Emalia Rushmare', 'Menino', 'EE INDIGENA CACIQUE TIMOTEO - MIRANDA'), ('Frasco Jonuzi', 'Menino', 'FETEC'), ('Ally Babalola', 'Menino', 'EE SEN FILINTO MULLER/IVINHEMA'), ('Michell Dawson', 'Menino', 'EE PROF JOÃO MAGIANO PINTO - TRES LAGOAS'), ('Padraig Zmitrichenko', 'Menino', 'IFMS - DOURADOS'), ('Sharia Bratton', 'Menino', 'E.E. JOSÉ GARCIA LEAL - PARANAIBA'), ('Keri Bachmann', 'Menina', 'IFMS - NAVIRAÍ'), ('Matti Franken', 'Menino', 'IFMS - DOURADOS'), ('Jacynth Creany', 'Menina', 'EE VIRIATO BANDEIRA - COXIM'), ('Antonia Calladine', 'Menina', 'EE PROF JOÃO MAGIANO PINTO - TRES LAGOAS'), ('Natty Giannassi', 'Menina', 'EE INDIGENA CACIQUE TIMOTEO - MIRANDA'), ('Tate Granleese', 'Menino', 'EE INDIGENA CACIQUE TIMÓTEO - MIRANDA'), ('Kurt Byles', 'Menina', 'EE PROFESSOR JOSÉ PEREIRA LINS - DOURADOS'), ('Freddy Osichev', 'Menino', 'EE PROFESSOR JOSÉ PEREIRA LINS - DOURADOS'), ('Corrine Searl', 'Menina', 'UFMS'), ('Liana Zanicchi', 'Menino', 'UFMS'), ('Cherri Gantzer', 'Menina', 'IFMS - NAVIRAÍ'), ('Happy Marrison', 'Menina', 'VAGO'), ('Harrie Wapple', 'Menina', 'IFMS - COXIM'), ('Sanford Iwanicki', 'Menino', 'IFMS - AQUIDAUANA'), ('Tony Stitle', 'Menino', 'EE MARIA DA GLORIA MUZZI FERREIRA - DOURADOS'), ('Emmalee Boriston', 'Menina', 'IFMS - COXIM'), ('Fayth Gillibrand', 'Menina', 'EE REYNALDO MASSI/IVINHEMA'), ('Mano Napolione', 'Menina', 'EE PROF JOÃO MAGIANO PINTO - TRES LAGOAS'), ('Bridie Chew', 'Menino', 'EE DOM BOSCO - CORUMBA'), ('Lina Ferrey', 'Menina', 'IFMS - COXIM'), ('Aluino Derobert', 'Menino', 'EE VIRIATO BANDEIRA - COXIM'), ('Toinette Barczynski', 'Menina', 'IFMS - NOVA ANDRADINA'), ('Hedi Phillcock', 'Menina', 'EE FLORIANO VIEGAS MACHADO - DOURADOS'), ('Fleurette Doding', 'Menino', 'UFMS-CPAN'), ('Allsun Quarmby', 'Menino', 'EE DOM BOSCO - CORUMBA'), ('Ursuline Melody', 'Menino', 'EE PROFª GENI MARQUES MAGALHÃES - PONTA PORÃ'), ('Skye Carme', 'Menino', 'EE PROFª GENI MARQUES MAGALHÃES - PONTA PORÃ'), ('Orelee Simoneschi', 'Menina', 'UFMS'), ('Harbert Hellwich', 'Menino', 'EE ADE MARQUES - PONTA PORÃ'), ('Yalonda Hold', 'Menino', 'IFMS - PONTA PORÃ'), ('Ephraim Ascrofte', 'Menina', 'EE JULIA GONCALVES PASSARINHO - CORUMBA'), ('Kristin Meredith', 'Menina', 'IFMS - NAVIRAÍ'), ('Cathe Smooth', 'Menino', 'IFMS - PONTA PORÃ'), ('Ursa Currey', 'Menina', 'UFMS'), ('Inger Jouhan', 'Menina', 'EE SEN FILINTO MULLER/IVINHEMA'), ('Neda Turri', 'Menino', 'EE SEN FILINTO MULLER'), ('Riordan Riddall', 'Menina', 'IFMS - NOVA ANDRADINA'), ('Mariejeanne Canepe', 'Menino', 'EE DOM BOSCO - CORUMBA'), ('Martyn Jurasek', 'Menina', 'E.E. PROFª GENI MARQUES MAGALHÃES - PONTA PORÃ'), ('Esmeralda Teers', 'Menino', 'EE MARIA DA GLORIA MUZZI FERREIRA - DOURADOS'), ('Brandtr Lapidus', 'Menina', 'EE CEL JOSÉ ALVES RIBEIRO - AQUIDAUANA'), ('Abagail Farlambe', 'Menino', 'EE INDIGENA CACIQUE TIMÓTEO - MIRANDA'), ('Arie Gervaise', 'Menina', 'EE INDIGENA CACIQUE TIMÓTEO - MIRANDA'), ('Corey Benini', 'Menina', 'EE MARIA DA GLORIA MUZZI FERREIRA - DOURADOS'), ('Hobard McJarrow', 'Menino', 'EE SEN FILINTO MULLER'), ('Domeniga Bernetti', 'Menina', 'IFMS - NOVA ANDRADINA'), ('Ludovico Coleshill', 'Menino', 'VAGO'), ('Modestia Willowby', 'Menina', 'UFMS-CPAN'), ('Leah Powelee', 'Menina', 'FETEC'), ('Ruprecht Akaster', 'Menina', 'E.E. JOSÉ GARCIA LEAL - PARANAIBA'), ('Cos Cella', 'Menina', 'EE JULIA GONCALVES PASSARINHO - CORUMBA'), ('Heinrik Romanini', 'Menino', 'IFMS - COXIM'), ('Ravi Frear', 'Menina', 'EE INDIGENA CACIQUE TIMOTEO - MIRANDA'), ('Dacie Gatchell', 'Menino', 'EE PROFESSOR JOSÉ PEREIRA LINS - DOURADOS'), ('Tobye Traill', 'Menino', 'EE INDIGENA CACIQUE TIMOTEO - MIRANDA'), ('Nichole Llewellyn', 'Menina', 'EE PROFª GENI MARQUES MAGALHÃES - PONTA PORÃ'), ('Bill Doust', 'Menina', 'VAGO'), ('Deeyn MacTerlagh', 'Menino', 'E.E. JOSÉ GARCIA LEAL - PARANAIBA'), ('Winni Moncreif', 'Menino', 'EE JULIA GONCALVES PASSARINHO - CORUMBA'), ('Paulie Purches', 'Menina', 'E.E. JOSÉ GARCIA LEAL - PARANAIBA'), ('Sascha Rosgen', 'Menina', 'EE JULIA GONCALVES PASSARINHO - CORUMBA'), ('Hussein Wooff', 'Menina', 'EE FLORIANO VIEGAS MACHADO - DOURADOS'), ('Else Bickerdike', 'Menino', 'EE Marechal Rondon / NOVA ANDRADINA'), ('Robinson Shapiro', 'Menino', 'IFMS - AQUIDAUANA'), ('Roi Salan', 'Menina', 'IFMS - COXIM'), ('Alissa Heardman', 'Menina', 'E PROF. JOSÉ JUAREZ R DE OLIVEIRA - ITAQUIRAÍ'), ('Brandy Casellas', 'Menino', 'UFMS-CPAN'), ('Shurlocke Baroch', 'Menino', 'EE CEL JOSÉ ALVES RIBEIRO - AQUIDAUANA'), ('Milly Sherewood', 'Menino', 'FETEC'), ('Serene Jahnig', 'Menino', 'FETEC'), ('Jerrold Dionisetti', 'Menino', 'EE SEN FILINTO MULLER/IVINHEMA'), ('Olva Attew', 'Menina', 'EE VIRIATO BANDEIRA - COXIM'), ('Giorgi Louth', 'Menina', 'EE SEN FILINTO MULLER/IVINHEMA'), ('Giovanna Harker', 'Menino', 'UFMS-CPTL'), ('Zachery Fessby', 'Menina', 'EE CEL JOSÉ ALVES RIBEIRO - AQUIDAUANA'), ('Valerie Laxen', 'Menino', 'VAGO'), ('Adelaide MacArdle', 'Menina', 'EE MARIA DA GLORIA MUZZI FERREIRA - DOURADOS'), ('Stoddard Bruckent', 'Menina', 'IFMS - PONTA PORÃ'), ('Brianna Crack', 'Menino', 'E.E. JOSÉ GARCIA LEAL - PARANAIBA'), ('Garv Iacopo', 'Menino', 'IFMS - AQUIDAUANA'), ('Jonathon Chamberlayne', 'Menina', 'IFMS - NAVIRAÍ'), ('Ethelda Addionisio', 'Menina', 'EE ADE MARQUES - PONTA PORÃ'), ('Celestia Duell', 'Menino', 'IFMS - PONTA PORÃ'), ('Rupert Tripett', 'Menina', 'EE DOM BOSCO - CORUMBA'), ('Sancho Fawlo', 'Menino', 'IFMS - NAVIRAÍ'), ('Mab Niset', 'Menino', 'EE FLORIANO VIEGAS MACHADO - DOURADOS'), ('Konrad Verrell', 'Menino', 'EE VIRIATO BANDEIRA - COXIM'), ('Melodee Feely', 'Menino', 'EE VIRIATO BANDEIRA/COXIM'), ('Fonz McAndrew', 'Menino', 'EE JULIA GONCALVES PASSARINHO - CORUMBA'), ('Lynne Gyurko', 'Menino', 'EE MIN JOÃO PAULO DOS REIS VELOSO - DOURADOS'), ('Minette Brolly', 'Menina', 'EE Marechal Rondon / NOVA ANDRADINA'), ('Barn Iaduccelli', 'Menino', 'FETEC'), ('Myca Biasi', 'Menino', 'IFMS - PONTA PORÃ'), ('Axe Cockling', 'Menino', 'EE VIRIATO BANDEIRA - COXIM'), ('Dani Alten', 'Menino', 'EE Marechal Rondon / NOVA ANDRADINA'), ('Sol Masey', 'Menina', 'UFMS-CPAN'), ('Christine Whitechurch', 'Menino', 'IFMS - NOVA ANDRADINA'), ('Adolphus Screase', 'Menino', 'EE JULIA GONCALVES PASSARINHO - CORUMBA'), ('Augustus Lehmann', 'Menina', 'IFMS - COXIM'), ('Theadora Corneil', 'Menina', 'UFMS-CPAN'), ('Merrel Howat', 'Menina', 'EE PROFESSOR JOSÉ PEREIRA LINS - DOURADOS'), ('Basilio Maryan', 'Menina', 'EE VIRIATO BANDEIRA/COXIM'), ('Nappy Fulstow', 'Menina', 'E.E. JOSÉ GARCIA LEAL - PARANAIBA'), ('Alberto Padgett', 'Menina', 'UFMS-CPTL'), ('Meyer Rayer', 'Menina', 'EE PROFESSOR JOSÉ PEREIRA LINS - DOURADOS'), ('Clyde Clixby', 'Menina', 'VAGO'), ('Marlow Granger', 'Menino', 'EE REYNALDO MASSI/IVINHEMA'), ('Kara-lynn Aime', 'Menina', 'E.E. JOSÉ GARCIA LEAL - PARANAIBA'), ('Aylmar Lamlin', 'Menino', 'EE MIN JOÃO PAULO DOS REIS VELOSO - DOURADOS'), ('Leticia Lintall', 'Menino', 'EE VIRIATO BANDEIRA/COXIM'), ('Ora McKechnie', 'Menina', 'EE JULIA GONCALVES PASSARINHO - CORUMBA'), ('Grenville Eickhoff', 'Menino', 'EE VIRIATO BANDEIRA - COXIM'), ('Trescha Challen', 'Menina', 'EE DOM BOSCO - CORUMBA'), ('Roderick Barbara', 'Menino', 'EE Marechal Rondon / NOVA ANDRADINA'), ('Carrie Stowte', 'Menina', 'EE Marechal Rondon / NOVA ANDRADINA'), ('Octavius Laydel', 'Menina', 'EE INDIGENA CACIQUE TIMÓTEO - MIRANDA'), ('Wilden Gooms', 'Menino', 'EE CEL JOSÉ ALVES RIBEIRO - AQUIDAUANA')]

# Definição dos quartos e suas capacidades
rooms = {0: [(0, 182), (1, 182), (2, 182)], 1: [(0, 182), (1, 182), (2, 182)], 2: [(0, 182), (1, 182), (2, 182)], 3: [(0, 182), (1, 182), (2, 182)], 4: [(0, 182), (1, 182), (2, 182)], 5: [(0, 182), (1, 182), (2, 182)], 6: [(0, 182), (1, 182), (2, 182)], 7: [(0, 182), (1, 182), (2, 182)], 8: [(0, 182), (1, 182), (2, 182)], 9: [(0, 182), (1, 182), (2, 182)], 10: [(0, 182), (1, 182), (2, 182)], 11: [(0, 182), (1, 182), (2, 182)], 12: [(0, 182), (1, 182), (2, 182)], 13: [(0, 182), (1, 182), (2, 182)], 14: [(0, 182), (1, 182), (2, 182)], 15: [(0, 182), (1, 182), (2, 182)], 16: [(0, 182), (1, 182), (2, 182)], 17: [(0, 182), (1, 182), (2, 182)], 18: [(0, 182), (1, 182), (2, 182)], 19: [(0, 182), (1, 182), (2, 182)], 20: [(0, 182), (1, 182), (2, 182)], 21: [(0, 182), (1, 182), (2, 182)], 22: [(0, 182), (1, 182), (2, 182)], 23: [(0, 182), (1, 182), (2, 182)], 24: [(0, 182), (1, 182), (2, 182)], 25: [(0, 182), (1, 182), (2, 182)], 26: [(0, 182), (1, 182), (2, 182)], 27: [(0, 182), (1, 182), (2, 182)], 28: [(0, 182), (1, 182), (2, 182)], 29: [(0, 182), (1, 182), (2, 182)], 30: [(0, 182), (1, 182), (2, 182)], 31: [(0, 182), (1, 182), (2, 182)], 32: [(0, 182), (1, 182), (2, 182)], 33: [(0, 182), (1, 182), (2, 182)], 34: [(0, 182), (1, 182), (2, 182)], 35: [(0, 182), (1, 182), (2, 182)], 36: [(0, 182), (1, 182), (2, 182)], 37: [(0, 182), (1, 182), (2, 182)], 38: [(0, 182), (1, 182), (2, 182)], 39: [(0, 182), (1, 182), (2, 182)], 40: [(0, 182), (1, 182), (2, 182)], 41: [(0, 182), (1, 182), (2, 182)], 42: [(0, 182), (1, 182), (2, 182)], 43: [(0, 182), (1, 182), (2, 182)], 44: [(0, 182), (1, 182), (2, 182)], 45: [(0, 182), (1, 182), (2, 182)], 46: [(0, 182), (1, 182), (2, 182)], 47: [(0, 182), (1, 182), (2, 182)], 48: [(0, 182), (1, 182), (2, 182)], 49: [(0, 182), (1, 182), (2, 182)], 50: [(0, 216), (1, 216), (2, 216)], 51: [(0, 216), (1, 216), (2, 216)], 52: [(0, 216), (1, 216), (2, 216)], 53: [(0, 216), (1, 216), (2, 216)], 54: [(0, 216), (1, 216), (2, 216)], 55: [(0, 216), (1, 216), (2, 216)], 56: [(0, 216), (1, 216), (2, 216)], 57: [(0, 216), (1, 216), (2, 216)], 58: [(0, 216), (1, 216), (2, 216)], 59: [(0, 216), (1, 216), (2, 216)], 60: [(0, 216), (1, 216), (2, 216)], 61: [(0, 216), (1, 216), (2, 216)], 62: [(0, 216), (1, 216), (2, 216)], 63: [(0, 216), (1, 216), (2, 216)], 64: [(0, 216), (1, 216), (2, 216)], 65: [(0, 216), (1, 216), (2, 216)], 66: [(0, 216), (1, 216), (2, 216)], 67: [(0, 216), (1, 216), (2, 216)], 68: [(0, 216), (1, 216), (2, 216)], 69: [(0, 216), (1, 216), (2, 216)], 70: [(0, 216), (1, 216), (2, 216)], 71: [(0, 216), (1, 216), (2, 216)], 72: [(0, 216), (1, 216), (2, 216)], 73: [(0, 216), (1, 216), (2, 216)], 74: [(0, 216), (1, 216), (2, 216)], 75: [(0, 216), (1, 216), (2, 216)], 76: [(0, 216), (1, 216), (2, 216)], 77: [(0, 216), (1, 216), (2, 216)], 78: [(0, 216), (1, 216), (2, 216)], 79: [(0, 216), (1, 216), (2, 216)], 80: [(0, 216), (1, 216), (2, 216)], 81: [(0, 216), (1, 216), (2, 216)], 82: [(0, 216), (1, 216), (2, 216)], 83: [(0, 216), (1, 216), (2, 216)], 84: [(0, 216), (1, 216), (2, 216)], 85: [(0, 216), (1, 216), (2, 216)], 86: [(0, 216), (1, 216), (2, 216)], 87: [(0, 216), (1, 216), (2, 216)], 88: [(0, 216), (1, 216), (2, 216)], 89: [(0, 216), (1, 216), (2, 216)], 90: [(0, 182), (1, 182), (2, 182)], 91: [(0, 182), (1, 182), (2, 182)], 92: [(0, 182), (1, 182), (2, 182)], 93: [(0, 182), (1, 182), (2, 182)], 94: [(0, 182), (1, 182), (2, 182)], 95: [(0, 182), (1, 182), (2, 182)], 96: [(0, 182), (1, 182), (2, 182)], 97: [(0, 182), (1, 182), (2, 182)], 98: [(0, 182), (1, 182), (2, 182)], 99: [(0, 182), (1, 182), (2, 182)], 100: [(0, 182), (1, 182), (2, 182)], 101: [(0, 182), (1, 182), (2, 182)], 102: [(0, 182), (1, 182), (2, 182)], 103: [(0, 182), (1, 182), (2, 182)], 104: [(0, 182), (1, 182), (2, 182)], 105: [(0, 182), (1, 182), (2, 182)], 106: [(0, 182), (1, 182), (2, 182)], 107: [(0, 182), (1, 182), (2, 182)], 108: [(0, 182), (1, 182), (2, 182)], 109: [(0, 182), (1, 182), (2, 182)], 110: [(0, 182), (1, 182), (2, 182)], 111: [(0, 148), (1, 148), (2, 148)], 112: [(0, 148), (1, 148), (2, 148)], 113: [(0, 148), (1, 148), (2, 148)], 114: [(0, 148), (1, 148), (2, 148)], 115: [(0, 148), (1, 148), (2, 148)], 116: [(0, 148), (1, 148), (2, 148)], 117: [(0, 148), (1, 148), (2, 148)], 118: [(0, 148), (1, 148), (2, 148)], 119: [(0, 148), (1, 148), (2, 148)], 120: [(0, 148), (1, 148), (2, 148)], 121: [(0, 148), (1, 148), (2, 148)], 122: [(0, 148), (1, 148), (2, 148)], 123: [(0, 148), (1, 148), (2, 148)], 124: [(0, 148), (1, 148), (2, 148)], 125: [(0, 148), (1, 148), (2, 148)], 126: [(0, 148), (1, 148), (2, 148)], 127: [(0, 148), (1, 148), (2, 148)], 128: [(0, 148), (1, 148), (2, 148)], 129: [(0, 148), (1, 148), (2, 148)], 130: [(0, 148), (1, 148), (2, 148)], 131: [(0, 148), (1, 148), (2, 148)], 132: [(0, 216), (1, 216), (2, 216)], 133: [(0, 216), (1, 216), (2, 216)], 134: [(0, 216), (1, 216), (2, 216)], 135: [(0, 216), (1, 216), (2, 216)], 136: [(0, 216), (1, 216), (2, 216)], 137: [(0, 216), (1, 216), (2, 216)], 138: [(0, 216), (1, 216), (2, 216)], 139: [(0, 216), (1, 216), (2, 216)], 140: [(0, 216), (1, 216), (2, 216)], 141: [(0, 216), (1, 216), (2, 216)], 142: [(0, 216), (1, 216), (2, 216)], 143: [(0, 216), (1, 216), (2, 216)], 144: [(0, 216), (1, 216), (2, 216)], 145: [(0, 216), (1, 216), (2, 216)], 146: [(0, 216), (1, 216), (2, 216)], 147: [(0, 216), (1, 216), (2, 216)], 148: [(0, 216), (1, 216), (2, 216)], 149: [(0, 216), (1, 216), (2, 216)], 150: [(0, 216), (1, 216), (2, 216)], 151: [(0, 216), (1, 216), (2, 216)], 152: [(0, 216), (1, 216), (2, 216)], 153: [(0, 216), (1, 216), (2, 216)], 154: [(0, 216), (1, 216), (2, 216)], 155: [(0, 216), (1, 216), (2, 216)], 156: [(0, 216), (1, 216), (2, 216)], 157: [(0, 216), (1, 216), (2, 216)], 158: [(0, 216), (1, 216), (2, 216)], 159: [(0, 216), (1, 216), (2, 216)], 160: [(0, 216), (1, 216), (2, 216)], 161: [(0, 216), (1, 216), (2, 216)], 162: [(0, 216), (1, 216), (2, 216)], 163: [(0, 216), (1, 216), (2, 216)], 164: [(0, 216), (1, 216), (2, 216)], 165: [(0, 216), (1, 216), (2, 216)], 166: [(0, 216), (1, 216), (2, 216)], 167: [(0, 216), (1, 216), (2, 216)], 168: [(0, 216), (1, 216), (2, 216)], 169: [(0, 216), (1, 216), (2, 216)], 170: [(0, 216), (1, 216), (2, 216)], 171: [(0, 216), (1, 216), (2, 216)], 172: [(0, 216), (1, 216), (2, 216)], 173: [(0, 216), (1, 216), (2, 216)], 174: [(0, 216), (1, 216), (2, 216)], 175: [(0, 216), (1, 216), (2, 216)], 176: [(0, 216), (1, 216), (2, 216)], 177: [(0, 216), (1, 216), (2, 216)], 178: [(0, 216), (1, 216), (2, 216)], 179: [(0, 216), (1, 216), (2, 216)], 180: [(0, 216), (1, 216), (2, 216)], 181: [(0, 216), (1, 216), (2, 216)], 182: [(0, 216), (1, 216), (2, 216)], 183: [(0, 216), (1, 216), (2, 216)], 184: [(0, 216), (1, 216), (2, 216)], 185: [(0, 216), (1, 216), (2, 216)], 186: [(0, 216), (1, 216), (2, 216)], 187: [(0, 216), (1, 216), (2, 216)], 188: [(0, 216), (1, 216), (2, 216)], 189: [(0, 216), (1, 216), (2, 216)], 190: [(0, 216), (1, 216), (2, 216)], 191: [(0, 216), (1, 216), (2, 216)], 192: [(0, 216), (1, 216), (2, 216)], 193: [(0, 216), (1, 216), (2, 216)], 194: [(0, 216), (1, 216), (2, 216)], 195: [(0, 216), (1, 216), (2, 216)], 196: [(0, 216), (1, 216), (2, 216)], 197: [(0, 216), (1, 216), (2, 216)], 198: [(0, 216), (1, 216), (2, 216)], 199: [(0, 216), (1, 216), (2, 216)], 200: [(0, 216), (1, 216), (2, 216)], 201: [(0, 216), (1, 216), (2, 216)], 202: [(0, 216), (1, 216), (2, 216)], 203: [(0, 216), (1, 216), (2, 216)], 204: [(0, 216), (1, 216), (2, 216)], 205: [(0, 216), (1, 216), (2, 216)], 206: [(0, 216), (1, 216), (2, 216)], 207: [(0, 216), (1, 216), (2, 216)], 208: [(0, 216), (1, 216), (2, 216)], 209: [(0, 216), (1, 216), (2, 216)], 210: [(0, 216), (1, 216), (2, 216)], 211: [(0, 216), (1, 216), (2, 216)], 212: [(0, 216), (1, 216), (2, 216)], 213: [(0, 216), (1, 216), (2, 216)], 214: [(0, 216), (1, 216), (2, 216)], 215: [(0, 216), (1, 216), (2, 216)], 216: [(0, 216), (1, 216), (2, 216)], 217: [(0, 216), (1, 216), (2, 216)], 218: [(0, 216), (1, 216), (2, 216)], 219: [(0, 216), (1, 216), (2, 216)], 220: [(0, 216), (1, 216), (2, 216)], 221: [(0, 216), (1, 216), (2, 216)], 222: [(0, 216), (1, 216), (2, 216)], 223: [(0, 216), (1, 216), (2, 216)], 224: [(0, 216), (1, 216), (2, 216)], 225: [(0, 216), (1, 216), (2, 216)], 226: [(0, 216), (1, 216), (2, 216)], 227: [(0, 216), (1, 216), (2, 216)], 228: [(0, 216), (1, 216), (2, 216)], 229: [(0, 216), (1, 216), (2, 216)], 230: [(0, 216), (1, 216), (2, 216)], 231: [(0, 216), (1, 216), (2, 216)], 232: [(0, 216), (1, 216), (2, 216)], 233: [(0, 216), (1, 216), (2, 216)], 234: [(0, 216), (1, 216), (2, 216)], 235: [(0, 216), (1, 216), (2, 216)], 236: [(0, 216), (1, 216), (2, 216)], 237: [(0, 216), (1, 216), (2, 216)], 238: [(0, 216), (1, 216), (2, 216)], 239: [(0, 216), (1, 216), (2, 216)], 240: [(0, 216), (1, 216), (2, 216)], 241: [(0, 216), (1, 216), (2, 216)], 242: [(0, 216), (1, 216), (2, 216)], 243: [(0, 216), (1, 216), (2, 216)], 244: [(0, 216), (1, 216), (2, 216)], 245: [(0, 216), (1, 216), (2, 216)], 246: [(0, 216), (1, 216), (2, 216)], 247: [(0, 216), (1, 216), (2, 216)], 248: [(0, 216), (1, 216), (2, 216)], 249: [(0, 216), (1, 216), (2, 216)], 250: [(0, 216), (1, 216), (2, 216)], 251: [(0, 216), (1, 216), (2, 216)], 252: [(0, 216), (1, 216), (2, 216)], 253: [(0, 216), (1, 216), (2, 216)], 254: [(0, 216), (1, 216), (2, 216)], 255: [(0, 216), (1, 216), (2, 216)], 256: [(0, 216), (1, 216), (2, 216)], 257: [(0, 216), (1, 216), (2, 216)], 258: [(0, 216), (1, 216), (2, 216)], 259: [(0, 216), (1, 216), (2, 216)], 260: [(0, 216), (1, 216), (2, 216)], 261: [(0, 216), (1, 216), (2, 216)], 262: [(0, 216), (1, 216), (2, 216)], 263: [(0, 216), (1, 216), (2, 216)], 264: [(0, 216), (1, 216), (2, 216)], 265: [(0, 216), (1, 216), (2, 216)], 266: [(0, 216), (1, 216), (2, 216)], 267: [(0, 216), (1, 216), (2, 216)], 268: [(0, 216), (1, 216), (2, 216)], 269: [(0, 216), (1, 216), (2, 216)], 270: [(0, 216), (1, 216), (2, 216)], 271: [(0, 216), (1, 216), (2, 216)], 272: [(0, 216), (1, 216), (2, 216)], 273: [(0, 216), (1, 216), (2, 216)], 274: [(0, 216), (1, 216), (2, 216)], 275: [(0, 216), (1, 216), (2, 216)], 276: [(0, 216), (1, 216), (2, 216)], 277: [(0, 216), (1, 216), (2, 216)], 278: [(0, 216), (1, 216), (2, 216)], 279: [(0, 216), (1, 216), (2, 216)], 280: [(0, 216), (1, 216), (2, 216)], 281: [(0, 216), (1, 216), (2, 216)], 282: [(0, 216), (1, 216), (2, 216)], 283: [(0, 216), (1, 216), (2, 216)], 284: [(0, 182), (1, 182), (2, 182)], 285: [(0, 182), (1, 182), (2, 182)], 286: [(0, 182), (1, 182), (2, 182)], 287: [(0, 182), (1, 182), (2, 182)], 288: [(0, 182), (1, 182), (2, 182)], 289: [(0, 182), (1, 182), (2, 182)], 290: [(0, 182), (1, 182), (2, 182)], 291: [(0, 182), (1, 182), (2, 182)], 292: [(0, 182), (1, 182), (2, 182)], 293: [(0, 182), (1, 182), (2, 182)], 294: [(0, 182), (1, 182), (2, 182)], 295: [(0, 182), (1, 182), (2, 182)], 296: [(0, 182), (1, 182), (2, 182)], 297: [(0, 182), (1, 182), (2, 182)], 298: [(0, 182), (1, 182), (2, 182)], 299: [(0, 182), (1, 182), (2, 182)], 300: [(0, 182), (1, 182), (2, 182)], 301: [(0, 182), (1, 182), (2, 182)], 302: [(0, 182), (1, 182), (2, 182)], 303: [(0, 182), (1, 182), (2, 182)], 304: [(0, 182), (1, 182), (2, 182)], 305: [(0, 182), (1, 182), (2, 182)], 306: [(0, 182), (1, 182), (2, 182)], 307: [(0, 182), (1, 182), (2, 182)], 308: [(0, 182), (1, 182), (2, 182)], 309: [(0, 182), (1, 182), (2, 182)], 310: [(0, 182), (1, 182), (2, 182)], 311: [(0, 182), (1, 182), (2, 182)], 312: [(0, 182), (1, 182), (2, 182)], 313: [(0, 182), (1, 182), (2, 182)]}

solucao = [
  1,0,
  2,0,
  1,1,
  2,1,
  2,2,
  1,2]

def imprimir_quartos(solucao):
 solucao_tuplas = [(solucao[i], solucao[i+1]) for i in range(0, len(solucao), 2)]
 for i in range(0, len(rooms)):
    print('Hospedes no quarto: ', i)
    for j in range(0, len(solucao_tuplas)):
      if solucao_tuplas[j][0] == i:
         print('Hospede ', guests[j][0])

def funcao_custo(solucao):
  preco_total = 0
  id_quarto = 0
  arrayDidSeen = []

  for i in range( len(solucao) // 2 ):
    if solucao[id_quarto] not in arrayDidSeen:
     arrayDidSeen.append(solucao[id_quarto])
     id_quarto_in_for = 0
     arrayGuests = []
     index = 0
    
     for j in range( len(solucao) // 2 ):
        if solucao[id_quarto_in_for] == solucao[id_quarto]:
          arrayGuests.append(guests[id_quarto_in_for//2])
          if solucao[id_quarto_in_for+1] == 0:
            index = id_quarto_in_for//2
        id_quarto_in_for += 2
     firstSchool = guests[index][2]
     firstGender = guests[index][1]
     #penalidades
     for guest in arrayGuests:
        if guest[2] != firstSchool:
          preco_total += 500
        if guest[1] != firstGender:
          preco_total += 250
    
     room = rooms[solucao[id_quarto]]
     preco_total += room[0][1] * len(arrayGuests)
    id_quarto += 2
  
  id_quarto = 0
  arrayRooms = [0]*len(rooms)

  for i in range( len(solucao) // 2 ):
    arrayRooms[solucao[id_quarto]] += 1
    id_quarto += 2

  for i in range( len(arrayRooms) ):
     if(len(rooms[i]) > arrayRooms[i] and arrayRooms[i] != 0):
        preco_total += 500
  
  return preco_total

def allocate_guests(rooms, guests):
    allocation = []  # Lista para armazenar a alocação de convidados
    room_count = {room: 0 for room in rooms}  # Dicionário para acompanhar quantos convidados foram alocados em cada quarto

    for guest_index, (_, _, _) in enumerate(guests):
        room = random.choice(list(rooms.keys()))  # Escolhe um quarto aleatório

        if room_count[room] < len(rooms[room]):  # Verifica se o quarto não excedeu sua capacidade
            allocation.extend([room, room_count[room]])  # Adiciona o quarto e a posição do convidado à alocação
            room_count[room] += 1  # Atualiza o contador de convidados no quarto
        else:
            for alt_room in rooms.keys():  # Se o quarto estiver cheio, tenta novamente em outro quarto
                if room_count[alt_room] < len(rooms[alt_room]):
                    allocation.extend([alt_room, room_count[alt_room]])  # Adiciona o quarto e a posição do convidado à alocação
                    room_count[alt_room] += 1  # Atualiza o contador de convidados no quarto
                    break

    return allocation

def pesquisa_randomica(funcao_custo):
  melhor_custo = 9999999
  melhor_soluc = []
  for i in range(0, 1000):
    solucao_random = allocate_guests(rooms, guests)
    custo = funcao_custo(solucao_random)
    if custo < melhor_custo:
      melhor_custo = custo
      melhor_soluc = solucao_random
  return melhor_soluc

def verify_dont_full_room(solucao, pos):
  arrayRooms = [0]*len(rooms)
  id_quarto=0
  for i in range( len(solucao) // 2 ):
    arrayRooms[solucao[id_quarto]] += 1
    id_quarto += 2
  if arrayRooms[solucao[pos]] + 1 <= len(rooms[solucao[pos]]):
     return True 
  else:
     return False

def troca_aleatoria(array1, array2):
    # Verifica se os arrays têm o mesmo tamanho
    aux = array1.copy()
    aux2 = array1.copy()
    indices_sort = array2.copy()
    random.shuffle(indices_sort)
    j = 0
    for i in array2:
       aux[i] = aux2[indices_sort[j]]
       j+= 1
    
    return aux

def mutacao_room(solucao):
  mutante = solucao.copy()          
  i = random.randint(0, len(mutante)-1)
  j = random.randint(0, len(mutante)-1)

  while i % 2 != 0 or j % 2 != 0:
    i = random.randint(0, len(mutante)-1)
    j = random.randint(0, len(mutante)-1)

  if (i != j) :
     aux = mutante[j]
     mutante[j] = mutante[i] 
     mutante[i] = aux
     return mutante
  return mutante

def mutacao_guests(solucao):
  mutante = solucao.copy()          
  index = random.choice([x for x in range(len(rooms)-1) if x % 2 == 0])
  array_in_mutante = []
  id_sol = 0
  for i in range(len(solucao) // 2):
     if(solucao[id_sol] == index):
        array_in_mutante.append(id_sol+1)
     id_sol += 2
  mutante = troca_aleatoria(mutante, array_in_mutante)
  return mutante

def revert_tupla(solucao):
   array = []
   id_array = 0

   for i in solucao:
      array.append(solucao[id_array][0])
      array.append(solucao[id_array][1])
      id_array += 1
   return array
   
def cruzamento(solucao1, solucao2):

   solucao1_tuplas = [(solucao1[i], solucao1[i+1]) for i in range(0, len(solucao1), 2)]
   solucao2_tuplas = [(solucao2[i], solucao2[i+1]) for i in range(0, len(solucao2), 2)]
   index = random.randint(1, (len(solucao1)//2) - 1)
   for i in range(0, (len(solucao1_tuplas)-index)):
      change = 0
      for j in range(0, len(solucao1_tuplas)):
         if solucao2_tuplas[i] == solucao1_tuplas[j]:
            change = 0
            break
         else:
            change = 1

      if change == 1:
         solucao1_tuplas[index+i] = solucao2_tuplas[i]
   return revert_tupla(solucao1_tuplas)

def genetico(funcao_custo, tamanho_populacao=1000, probabilidade_mutacao=0.8,
             elitismo=0.15,numero_geracoes=3000):
   populacao = []

   for i in range(tamanho_populacao):
      solucao = allocate_guests(rooms, guests)
      populacao.append(solucao)
    
   numero_elitismo = int(elitismo * tamanho_populacao)
   
   for i in range(numero_geracoes):
      custos = [(funcao_custo(individuo), individuo) for individuo in populacao]
      custos.sort()
      individuos_ordenados = [individuo for (custo, individuo) in custos]

      populacao = individuos_ordenados[0:numero_elitismo]
      
      while len(populacao) < tamanho_populacao:
         if random.random() < probabilidade_mutacao:
            m = random.randint(0, numero_elitismo)
            populacao.append(mutacao_room(individuos_ordenados[m]))
         else:
            c1 = random.randint(0, numero_elitismo)
            c2 = random.randint(0, numero_elitismo)
            if c1 > c2 :
             populacao.append(cruzamento(individuos_ordenados[c1], individuos_ordenados[c2]))
            else: 
             populacao.append(cruzamento(individuos_ordenados[c2], individuos_ordenados[c1]))
   return custos[0][1]
   
def genetico2(funcao_custo, tamanho_populacao=150, probabilidade_mutacao=0.8,
             elitismo=0.2,numero_geracoes= 10):
   populacao = []

   for i in range(tamanho_populacao):
      solucao = allocate_guests(rooms, guests)
      populacao.append(solucao)
    
   numero_elitismo = int(elitismo * tamanho_populacao)
   
   for i in range(numero_geracoes):
      custos = [(funcao_custo(individuo), individuo) for individuo in populacao]
      custos.sort()
      individuos_ordenados = [individuo for (custo, individuo) in custos]

      populacao = individuos_ordenados[0:numero_elitismo]
      
      while len(populacao) < tamanho_populacao:
         if random.random() < probabilidade_mutacao:
            m = random.randint(0, numero_elitismo)
            populacao.append(mutacao_guests(individuos_ordenados[m]))
         else:
            c1 = random.randint(0, numero_elitismo)
            c2 = random.randint(0, numero_elitismo)
            if c1 > c2 :
             populacao.append(cruzamento(individuos_ordenados[c1], individuos_ordenados[c2]))
            else: 
             populacao.append(cruzamento(individuos_ordenados[c2], individuos_ordenados[c1]))
   return custos[0][1]
       
def genetico3(funcao_custo, tamanho_populacao=500, probabilidade_mutacao=0.8,
             elitismo=0.2,numero_geracoes= 1000):
   populacao = []

   for i in range(tamanho_populacao):
      solucao = allocate_guests(rooms, guests)
      populacao.append(solucao)
    
   numero_elitismo = int(elitismo * tamanho_populacao)
   
   for i in range(numero_geracoes):
      custos = [(funcao_custo(individuo), individuo) for individuo in populacao]
      custos.sort()
      individuos_ordenados = [individuo for (custo, individuo) in custos]

      populacao = individuos_ordenados[0:numero_elitismo]
      
      while len(populacao) < tamanho_populacao:
         if random.random() < probabilidade_mutacao:
            if random.random() < 0.5:
              m = random.randint(0, numero_elitismo)
              populacao.append(mutacao_room(individuos_ordenados[m]))
            else:
               m = random.randint(0, numero_elitismo)
               populacao.append(mutacao_guests(individuos_ordenados[m]))
         else:
            c1 = random.randint(0, numero_elitismo)
            c2 = random.randint(0, numero_elitismo)
            if c1 > c2 :
             populacao.append(cruzamento(individuos_ordenados[c1], individuos_ordenados[c2]))
            else: 
             populacao.append(cruzamento(individuos_ordenados[c2], individuos_ordenados[c1]))
   return custos[0][1]

'''  
mediaPr = 0
mediaGen1 = 0
mediaGen2 = 0
mediaGen3 = 0

menorPr = 9999999
menorGen1 = 9999999
menorGen2 = 9999999
menorGen3 = 9999999

for i in range(0,10):
   #pr = pesquisa_randomica(funcao_custo)           
   g = genetico(funcao_custo)
   #g2 = genetico2(funcao_custo)
   #g3 = genetico3(funcao_custo)
   #fc1 = funcao_custo(pr)
   fc2 = funcao_custo(g)
   #fc3 = funcao_custo(g2)
   #fc4 = funcao_custo(g3)

   #mediaPr += fc1
   mediaGen1 += fc2
   #mediaGen2 += fc3
   #mediaGen3 += fc4

   #if menorPr > fc1:
   #   menorPr = fc1
   if menorGen1 > fc2:
      menorGen1 = fc2
   #if menorGen2 > fc3:
   #   menorGen2 = fc3
   #if menorGen3 > fc4:
   #   menorGen3 = fc4

menor2 = 999999999
solucao = []

if menorPr < menor2:
   menor2 = menorPr
   solucao = pr
   print('Menor Final PR')
if menorGen1 < menor2:
   menor2 = menorGen1
   solucao = g
   print('Menor Final G1')
if menorGen2 < menor2:
   menor2 = menorGen2
   solucao = g2
   print('Menor Final G2')
if menorGen3 < menor2:
   menor2 = menorGen3
   solucao = g3
   print('Menor Final G3')

'''

solucao = genetico(funcao_custo)
fc2 = funcao_custo(solucao)
print(solucao)
print(fc2)
imprimir_quartos(solucao)