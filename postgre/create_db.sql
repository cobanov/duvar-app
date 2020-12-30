-- Table: dneme.table1

-- DROP TABLE dneme.table1;

CREATE TABLE dneme.table1
(
    message_id integer NOT NULL DEFAULT nextval('dneme.table1_message_id_seq'::regclass),
    content character varying(280) COLLATE pg_catalog."default" NOT NULL,
    date timestamp with time zone,
    vote smallint DEFAULT 0,
    CONSTRAINT table1_pkey PRIMARY KEY (message_id)
)

TABLESPACE pg_default;

ALTER TABLE dneme.table1
    OWNER to postgres;
