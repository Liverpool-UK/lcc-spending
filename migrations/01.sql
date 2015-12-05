
CREATE TABLE over_500(
    id integer NOT NULL,
    service_area text,
    expense_type text,
    sap_document text,
    posting_date timestamp without time zone,
    vendor text,
    amount money,
    month integer,
    year integer
);


CREATE SEQUENCE over_500_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE ONLY over_500 ALTER COLUMN id SET DEFAULT nextval('over_500_id_seq'::regclass);
ALTER TABLE ONLY over_500 ADD CONSTRAINT over_500_pkey PRIMARY KEY (id);

