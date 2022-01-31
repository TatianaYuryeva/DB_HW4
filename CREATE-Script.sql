create table if not exists Genre (
	id serial primary key,
	title varchar(100) not null);

create table if not exists Artist (
	id serial primary key,
	name varchar(100) not null);

create table if not exists GenreArtist (
	genre_id integer references Genre(id),
	artist_id integer references Artist(id), 
	constraint pk primary key (genre_id, artist_id));

create table if not exists Album (
	id serial primary key,
	title varchar (100) not null,
	release_year integer not null);
	
create table if not exists ArtistAlbum (
	artist_id integer references Artist(id),
	album_id integer references Album(id),
	constraint pk2 primary key (artist_id, album_id));

create table if not exists Track (
	id serial primary key,
	title varchar (100) not null,
	track_length integer not null,
	album_id integer references Album(id));

create table if not exists Collection (
	id serial primary key,
	title varchar (100) not null,
	release_year integer not null);

create table if not exists CollectionTrack (
	collection_id integer references Collection(id),
	track_id integer references Track(id),
	constraint pk3 primary key (collection_id, track_id));



