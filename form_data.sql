PGDMP                          {            Pedal_Shaale    15.3    15.3                0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            	           1262    16402    Pedal_Shaale    DATABASE     �   CREATE DATABASE "Pedal_Shaale" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'English_India.1252';
    DROP DATABASE "Pedal_Shaale";
                postgres    false            �            1259    16404 	   form_data    TABLE     �   CREATE TABLE public.form_data (
    id integer NOT NULL,
    name character varying,
    email character varying,
    contact character varying,
    address character varying,
    slot_date date
);
    DROP TABLE public.form_data;
       public         heap    postgres    false            �            1259    16403    form_data_id_seq    SEQUENCE     �   CREATE SEQUENCE public.form_data_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.form_data_id_seq;
       public          postgres    false    215            
           0    0    form_data_id_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE public.form_data_id_seq OWNED BY public.form_data.id;
          public          postgres    false    214            q           2604    16407    form_data id    DEFAULT     l   ALTER TABLE ONLY public.form_data ALTER COLUMN id SET DEFAULT nextval('public.form_data_id_seq'::regclass);
 ;   ALTER TABLE public.form_data ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    215    214    215                      0    16404 	   form_data 
   TABLE DATA           Q   COPY public.form_data (id, name, email, contact, address, slot_date) FROM stdin;
    public          postgres    false    215   	                  0    0    form_data_id_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('public.form_data_id_seq', 7, true);
          public          postgres    false    214            s           2606    16411    form_data form_data_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public.form_data
    ADD CONSTRAINT form_data_pkey PRIMARY KEY (id);
 B   ALTER TABLE ONLY public.form_data DROP CONSTRAINT form_data_pkey;
       public            postgres    false    215               �   x����n�0�g�)� IQ�[;e�ѵ�6b��Jj
�}��@
萁�r��N@���p�i��4�@�����Ӊ�Do�wᕮmn��;g�1J�'�����*����\��?�T
����N1,�k�?��K�!T�{9�g�Z_�������jYV����@�R)���{ho�R����d��S\����b�BS���r/p/��n���Fk%Qm���K��z     