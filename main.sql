/*
 Navicat Premium Data Transfer

 Source Server         : Ass
 Source Server Type    : SQLite
 Source Server Version : 3021000
 Source Schema         : main

 Target Server Type    : SQLite
 Target Server Version : 3021000
 File Encoding         : 65001

 Date: 21/09/2020 21:14:51
*/

PRAGMA foreign_keys = false;

-- ----------------------------
-- Table structure for Aconchego_comment
-- ----------------------------
DROP TABLE IF EXISTS "Aconchego_comment";
CREATE TABLE "Aconchego_comment" (
  "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
  "autor" varchar(255) NOT NULL,
  "comment" varchar(255) NOT NULL
);

-- ----------------------------
-- Records of Aconchego_comment
-- ----------------------------
INSERT INTO "Aconchego_comment" VALUES (1, 'Jerry Mouse', '"Working in conjunction with humanitarian aid agencies, we have supported programmes to help alleviate human suffering.');
INSERT INTO "Aconchego_comment" VALUES (3, 'Micky Mouse', '"Working in conjunction with humanitarian aid agencies, we have supported programmes to help alleviate human suffering.');
INSERT INTO "Aconchego_comment" VALUES (4, 'Emerson Cardoso', '"Las trip to pemba was amazing, i cant wait to do it again "');
INSERT INTO "Aconchego_comment" VALUES (5, 'Joao Jose', '"Working in conjunction with humanitarian aid agencies.');
INSERT INTO "Aconchego_comment" VALUES (6, 'Erick Jose', '"Working in conjunction with humanitarian aid agencies.');
INSERT INTO "Aconchego_comment" VALUES (7, 'Mike John', '"Working in conjunction with humanitarian aid agencies.');
INSERT INTO "Aconchego_comment" VALUES (8, 'Mikelson Kodaline', '"Working in conjunction with humanitarian aid agencies.');
INSERT INTO "Aconchego_comment" VALUES (9, 'Martin Garrix', '"Working in conjunction with humanitarian aid agencies.');
INSERT INTO "Aconchego_comment" VALUES (10, 'Zayn Malick', '"Working in conjunction with humanitarian aid agencies.');
INSERT INTO "Aconchego_comment" VALUES (11, 'Liam Paim', '"Working in conjunction with humanitarian aid agencies.');
INSERT INTO "Aconchego_comment" VALUES (12, 'Alessia Cara', '"Working in conjunction with humanitarian aid agencies.');
INSERT INTO "Aconchego_comment" VALUES (13, 'Sam Smith', '"Working in conjunction with humanitarian aid agencies.');

-- ----------------------------
-- Table structure for Aconchego_hotel
-- ----------------------------
DROP TABLE IF EXISTS "Aconchego_hotel";
CREATE TABLE "Aconchego_hotel" (
  "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
  "name" varchar(255) NOT NULL,
  "localizacao" varchar(255) NOT NULL,
  "descricao" text NOT NULL,
  "categoria" integer NOT NULL,
  "price" integer NOT NULL,
  "cover" varchar(255) NOT NULL
);

-- ----------------------------
-- Records of Aconchego_hotel
-- ----------------------------
INSERT INTO "Aconchego_hotel" VALUES (1, 'Wimbi Sun', 'Pemba, Mozambique', 'There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don''t look even slightly believable.', 3, 4365, 'img/place/3.png');
INSERT INTO "Aconchego_hotel" VALUES (2, 'Kauri Resort', 'Pemba, Mozambique', 'There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don''t look even slightly believable.', 4, 2343, 'img/place/2.png');
INSERT INTO "Aconchego_hotel" VALUES (3, 'Kirimizi', 'Pemba, Mozambique', 'There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don''t look even slightly believable.', 5, 5643, 'img/place/1.png');
INSERT INTO "Aconchego_hotel" VALUES (4, 'Ralphs', 'Pemba, Mozambique', 'There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don''t look even slightly believable.', 2, 56456, 'img/place/5.png');

-- ----------------------------
-- Table structure for Aconchego_hotel_fotos
-- ----------------------------
DROP TABLE IF EXISTS "Aconchego_hotel_fotos";
CREATE TABLE "Aconchego_hotel_fotos" (
  "path" varchar(255) NOT NULL,
  "hotel_id" integer,
  "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
  FOREIGN KEY ("hotel_id") REFERENCES "Aconchego_hotel" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION DEFERRABLE INITIALLY DEFERRED
);

-- ----------------------------
-- Records of Aconchego_hotel_fotos
-- ----------------------------
INSERT INTO "Aconchego_hotel_fotos" VALUES ('img/elements/g1.jpg', 1, 1);
INSERT INTO "Aconchego_hotel_fotos" VALUES ('img/elements/g2.jpg', 1, 2);
INSERT INTO "Aconchego_hotel_fotos" VALUES ('img/elements/g3.jpg', 2, 3);
INSERT INTO "Aconchego_hotel_fotos" VALUES ('img/elements/g4.jpg', 2, 4);
INSERT INTO "Aconchego_hotel_fotos" VALUES ('img/elements/g5.jpg', 2, 5);
INSERT INTO "Aconchego_hotel_fotos" VALUES ('img/elements/g6.jpg', 3, 6);
INSERT INTO "Aconchego_hotel_fotos" VALUES ('img/elements/g7.jpg', 4, 7);
INSERT INTO "Aconchego_hotel_fotos" VALUES ('img/elements/g8.jpg', 4, 8);

-- ----------------------------
-- Table structure for Aconchego_reserva
-- ----------------------------
DROP TABLE IF EXISTS "Aconchego_reserva";
CREATE TABLE "Aconchego_reserva" (
  "checkindate" date,
  "checkoutdate" date,
  "adultos" integer NOT NULL,
  "crianca" integer NOT NULL,
  "preco" integer NOT NULL,
  "hotel_id" integer,
  "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
  FOREIGN KEY ("hotel_id") REFERENCES "Aconchego_hotel" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION DEFERRABLE INITIALLY DEFERRED
);

-- ----------------------------
-- Records of Aconchego_reserva
-- ----------------------------
INSERT INTO "Aconchego_reserva" VALUES ('2111-09-29', '2111-09-29', 1, 1, 0, NULL, 3);
INSERT INTO "Aconchego_reserva" VALUES ('2020-09-14', '2020-09-17', 1, 2, 0, NULL, 4);

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS "auth_group";
CREATE TABLE "auth_group" (
  "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
  "name" varchar(150) NOT NULL,
  UNIQUE ("name" ASC)
);

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS "auth_group_permissions";
CREATE TABLE "auth_group_permissions" (
  "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
  "group_id" integer NOT NULL,
  "permission_id" integer NOT NULL,
  FOREIGN KEY ("group_id") REFERENCES "auth_group" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION DEFERRABLE INITIALLY DEFERRED,
  FOREIGN KEY ("permission_id") REFERENCES "auth_permission" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION DEFERRABLE INITIALLY DEFERRED
);

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS "auth_permission";
CREATE TABLE "auth_permission" (
  "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
  "content_type_id" integer NOT NULL,
  "codename" varchar(100) NOT NULL,
  "name" varchar(255) NOT NULL,
  FOREIGN KEY ("content_type_id") REFERENCES "django_content_type" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION DEFERRABLE INITIALLY DEFERRED
);

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO "auth_permission" VALUES (1, 1, 'add_logentry', 'Can add log entry');
INSERT INTO "auth_permission" VALUES (2, 1, 'change_logentry', 'Can change log entry');
INSERT INTO "auth_permission" VALUES (3, 1, 'delete_logentry', 'Can delete log entry');
INSERT INTO "auth_permission" VALUES (4, 1, 'view_logentry', 'Can view log entry');
INSERT INTO "auth_permission" VALUES (5, 2, 'add_permission', 'Can add permission');
INSERT INTO "auth_permission" VALUES (6, 2, 'change_permission', 'Can change permission');
INSERT INTO "auth_permission" VALUES (7, 2, 'delete_permission', 'Can delete permission');
INSERT INTO "auth_permission" VALUES (8, 2, 'view_permission', 'Can view permission');
INSERT INTO "auth_permission" VALUES (9, 3, 'add_group', 'Can add group');
INSERT INTO "auth_permission" VALUES (10, 3, 'change_group', 'Can change group');
INSERT INTO "auth_permission" VALUES (11, 3, 'delete_group', 'Can delete group');
INSERT INTO "auth_permission" VALUES (12, 3, 'view_group', 'Can view group');
INSERT INTO "auth_permission" VALUES (13, 4, 'add_user', 'Can add user');
INSERT INTO "auth_permission" VALUES (14, 4, 'change_user', 'Can change user');
INSERT INTO "auth_permission" VALUES (15, 4, 'delete_user', 'Can delete user');
INSERT INTO "auth_permission" VALUES (16, 4, 'view_user', 'Can view user');
INSERT INTO "auth_permission" VALUES (17, 5, 'add_contenttype', 'Can add content type');
INSERT INTO "auth_permission" VALUES (18, 5, 'change_contenttype', 'Can change content type');
INSERT INTO "auth_permission" VALUES (19, 5, 'delete_contenttype', 'Can delete content type');
INSERT INTO "auth_permission" VALUES (20, 5, 'view_contenttype', 'Can view content type');
INSERT INTO "auth_permission" VALUES (21, 6, 'add_session', 'Can add session');
INSERT INTO "auth_permission" VALUES (22, 6, 'change_session', 'Can change session');
INSERT INTO "auth_permission" VALUES (23, 6, 'delete_session', 'Can delete session');
INSERT INTO "auth_permission" VALUES (24, 6, 'view_session', 'Can view session');
INSERT INTO "auth_permission" VALUES (25, 7, 'add_hotel', 'Can add hotel');
INSERT INTO "auth_permission" VALUES (26, 7, 'change_hotel', 'Can change hotel');
INSERT INTO "auth_permission" VALUES (27, 7, 'delete_hotel', 'Can delete hotel');
INSERT INTO "auth_permission" VALUES (28, 7, 'view_hotel', 'Can view hotel');
INSERT INTO "auth_permission" VALUES (29, 8, 'add_hotel_fotos', 'Can add hotel_ fotos');
INSERT INTO "auth_permission" VALUES (30, 8, 'change_hotel_fotos', 'Can change hotel_ fotos');
INSERT INTO "auth_permission" VALUES (31, 8, 'delete_hotel_fotos', 'Can delete hotel_ fotos');
INSERT INTO "auth_permission" VALUES (32, 8, 'view_hotel_fotos', 'Can view hotel_ fotos');
INSERT INTO "auth_permission" VALUES (33, 9, 'add_room', 'Can add room');
INSERT INTO "auth_permission" VALUES (34, 9, 'change_room', 'Can change room');
INSERT INTO "auth_permission" VALUES (35, 9, 'delete_room', 'Can delete room');
INSERT INTO "auth_permission" VALUES (36, 9, 'view_room', 'Can view room');
INSERT INTO "auth_permission" VALUES (37, 10, 'add_room_fotos', 'Can add room_ fotos');
INSERT INTO "auth_permission" VALUES (38, 10, 'change_room_fotos', 'Can change room_ fotos');
INSERT INTO "auth_permission" VALUES (39, 10, 'delete_room_fotos', 'Can delete room_ fotos');
INSERT INTO "auth_permission" VALUES (40, 10, 'view_room_fotos', 'Can view room_ fotos');
INSERT INTO "auth_permission" VALUES (41, 11, 'add_reserva', 'Can add reserva');
INSERT INTO "auth_permission" VALUES (42, 11, 'change_reserva', 'Can change reserva');
INSERT INTO "auth_permission" VALUES (43, 11, 'delete_reserva', 'Can delete reserva');
INSERT INTO "auth_permission" VALUES (44, 11, 'view_reserva', 'Can view reserva');
INSERT INTO "auth_permission" VALUES (45, 12, 'add_comment', 'Can add comment');
INSERT INTO "auth_permission" VALUES (46, 12, 'change_comment', 'Can change comment');
INSERT INTO "auth_permission" VALUES (47, 12, 'delete_comment', 'Can delete comment');
INSERT INTO "auth_permission" VALUES (48, 12, 'view_comment', 'Can view comment');

-- ----------------------------
-- Table structure for auth_user
-- ----------------------------
DROP TABLE IF EXISTS "auth_user";
CREATE TABLE "auth_user" (
  "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
  "password" varchar(128) NOT NULL,
  "last_login" datetime,
  "is_superuser" bool NOT NULL,
  "username" varchar(150) NOT NULL,
  "last_name" varchar(150) NOT NULL,
  "email" varchar(254) NOT NULL,
  "is_staff" bool NOT NULL,
  "is_active" bool NOT NULL,
  "date_joined" datetime NOT NULL,
  "first_name" varchar(150) NOT NULL,
  UNIQUE ("username" ASC)
);

-- ----------------------------
-- Records of auth_user
-- ----------------------------
INSERT INTO "auth_user" VALUES (1, 'pbkdf2_sha256$216000$BRd1OHb9gTos$8HWt7fmFUcXxpENgaBOht1ZfK4EG1d5ooBPltU6DRsQ=', '2020-09-21 09:28:02.523769', 1, 'emerson', '', 'hemersonycardoso@gmail.com', 1, 1, '2020-09-21 09:27:18.858934', '');

-- ----------------------------
-- Table structure for auth_user_groups
-- ----------------------------
DROP TABLE IF EXISTS "auth_user_groups";
CREATE TABLE "auth_user_groups" (
  "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
  "user_id" integer NOT NULL,
  "group_id" integer NOT NULL,
  FOREIGN KEY ("user_id") REFERENCES "auth_user" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION DEFERRABLE INITIALLY DEFERRED,
  FOREIGN KEY ("group_id") REFERENCES "auth_group" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION DEFERRABLE INITIALLY DEFERRED
);

-- ----------------------------
-- Table structure for auth_user_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS "auth_user_user_permissions";
CREATE TABLE "auth_user_user_permissions" (
  "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
  "user_id" integer NOT NULL,
  "permission_id" integer NOT NULL,
  FOREIGN KEY ("user_id") REFERENCES "auth_user" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION DEFERRABLE INITIALLY DEFERRED,
  FOREIGN KEY ("permission_id") REFERENCES "auth_permission" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION DEFERRABLE INITIALLY DEFERRED
);

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS "django_admin_log";
CREATE TABLE "django_admin_log" (
  "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
  "action_time" datetime NOT NULL,
  "object_id" text,
  "object_repr" varchar(200) NOT NULL,
  "change_message" text NOT NULL,
  "content_type_id" integer,
  "user_id" integer NOT NULL,
  "action_flag" smallint unsigned NOT NULL,
  FOREIGN KEY ("content_type_id") REFERENCES "django_content_type" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION DEFERRABLE INITIALLY DEFERRED,
  FOREIGN KEY ("user_id") REFERENCES "auth_user" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION DEFERRABLE INITIALLY DEFERRED,
   ("action_flag" >= 0)
);

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS "django_content_type";
CREATE TABLE "django_content_type" (
  "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
  "app_label" varchar(100) NOT NULL,
  "model" varchar(100) NOT NULL
);

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO "django_content_type" VALUES (1, 'admin', 'logentry');
INSERT INTO "django_content_type" VALUES (2, 'auth', 'permission');
INSERT INTO "django_content_type" VALUES (3, 'auth', 'group');
INSERT INTO "django_content_type" VALUES (4, 'auth', 'user');
INSERT INTO "django_content_type" VALUES (5, 'contenttypes', 'contenttype');
INSERT INTO "django_content_type" VALUES (6, 'sessions', 'session');
INSERT INTO "django_content_type" VALUES (7, 'Aconchego', 'hotel');
INSERT INTO "django_content_type" VALUES (8, 'Aconchego', 'hotel_fotos');
INSERT INTO "django_content_type" VALUES (9, 'Aconchego', 'room');
INSERT INTO "django_content_type" VALUES (10, 'Aconchego', 'room_fotos');
INSERT INTO "django_content_type" VALUES (11, 'Aconchego', 'reserva');
INSERT INTO "django_content_type" VALUES (12, 'Aconchego', 'comment');

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS "django_migrations";
CREATE TABLE "django_migrations" (
  "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
  "app" varchar(255) NOT NULL,
  "name" varchar(255) NOT NULL,
  "applied" datetime NOT NULL
);

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO "django_migrations" VALUES (1, 'Aconchego', '0001_initial', '2020-09-16 13:19:30.885261');
INSERT INTO "django_migrations" VALUES (2, 'contenttypes', '0001_initial', '2020-09-16 13:19:31.217370');
INSERT INTO "django_migrations" VALUES (3, 'auth', '0001_initial', '2020-09-16 13:19:31.524428');
INSERT INTO "django_migrations" VALUES (4, 'admin', '0001_initial', '2020-09-16 13:19:31.814241');
INSERT INTO "django_migrations" VALUES (5, 'admin', '0002_logentry_remove_auto_add', '2020-09-16 13:19:32.354918');
INSERT INTO "django_migrations" VALUES (6, 'admin', '0003_logentry_add_action_flag_choices', '2020-09-16 13:19:32.624708');
INSERT INTO "django_migrations" VALUES (7, 'contenttypes', '0002_remove_content_type_name', '2020-09-16 13:19:32.916272');
INSERT INTO "django_migrations" VALUES (8, 'auth', '0002_alter_permission_name_max_length', '2020-09-16 13:19:33.199536');
INSERT INTO "django_migrations" VALUES (9, 'auth', '0003_alter_user_email_max_length', '2020-09-16 13:19:33.564282');
INSERT INTO "django_migrations" VALUES (10, 'auth', '0004_alter_user_username_opts', '2020-09-16 13:19:33.806746');
INSERT INTO "django_migrations" VALUES (11, 'auth', '0005_alter_user_last_login_null', '2020-09-16 13:19:34.125570');
INSERT INTO "django_migrations" VALUES (12, 'auth', '0006_require_contenttypes_0002', '2020-09-16 13:19:34.305372');
INSERT INTO "django_migrations" VALUES (13, 'auth', '0007_alter_validators_add_error_messages', '2020-09-16 13:19:34.636011');
INSERT INTO "django_migrations" VALUES (14, 'auth', '0008_alter_user_username_max_length', '2020-09-16 13:19:34.921411');
INSERT INTO "django_migrations" VALUES (15, 'auth', '0009_alter_user_last_name_max_length', '2020-09-16 13:19:35.249699');
INSERT INTO "django_migrations" VALUES (16, 'auth', '0010_alter_group_name_max_length', '2020-09-16 13:19:35.626690');
INSERT INTO "django_migrations" VALUES (17, 'auth', '0011_update_proxy_permissions', '2020-09-16 13:19:35.888528');
INSERT INTO "django_migrations" VALUES (18, 'auth', '0012_alter_user_first_name_max_length', '2020-09-16 13:19:36.104392');
INSERT INTO "django_migrations" VALUES (19, 'sessions', '0001_initial', '2020-09-16 13:19:36.688270');
INSERT INTO "django_migrations" VALUES (20, 'Aconchego', '0002_auto_20200916_1628', '2020-09-16 14:30:16.267526');
INSERT INTO "django_migrations" VALUES (21, 'Aconchego', '0003_auto_20200920_0746', '2020-09-20 05:48:46.828423');
INSERT INTO "django_migrations" VALUES (22, 'Aconchego', '0002_reserva', '2020-09-20 21:24:10.637718');
INSERT INTO "django_migrations" VALUES (23, 'Aconchego', '0003_auto_20200921_0026', '2020-09-20 22:27:03.131909');
INSERT INTO "django_migrations" VALUES (24, 'Aconchego', '0004_auto_20200921_1125', '2020-09-21 09:25:28.509509');
INSERT INTO "django_migrations" VALUES (25, 'Aconchego', '0005_auto_20200921_1752', '2020-09-21 15:52:56.214171');
INSERT INTO "django_migrations" VALUES (26, 'Aconchego', '0006_comment', '2020-09-21 16:10:20.913205');

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS "django_session";
CREATE TABLE "django_session" (
  "session_key" varchar(40) NOT NULL,
  "session_data" text NOT NULL,
  "expire_date" datetime NOT NULL,
  PRIMARY KEY ("session_key")
);

-- ----------------------------
-- Records of django_session
-- ----------------------------
INSERT INTO "django_session" VALUES ('2cbtccyhvmieo6fn92tei9mjpcodcs9y', '.eJxVjEEOgjAQRe_StWk6tFOoS_eegUw7M4IaSCisjHdXEha6_e-9_zI9bevQb1WWfmRzNmBOv1um8pBpB3yn6TbbMk_rMma7K_ag1V5nluflcP8OBqrDt9YoqAAOc-EOXBbfgrpIlNBDkxADpBQ6ZSwNsQCLags-xRByRN-a9wfcLzd5:1kKI78:5Hu6oaHhdo8kq0ixEIen0uvp1n9x-rXsp4_DYQ1Yhw8', '2020-10-05 09:28:02.634792');

-- ----------------------------
-- Table structure for sqlite_sequence
-- ----------------------------
DROP TABLE IF EXISTS "sqlite_sequence";
CREATE TABLE "sqlite_sequence" (
  "name",
  "seq"
);

-- ----------------------------
-- Records of sqlite_sequence
-- ----------------------------
INSERT INTO "sqlite_sequence" VALUES ('django_migrations', 26);
INSERT INTO "sqlite_sequence" VALUES ('django_admin_log', 0);
INSERT INTO "sqlite_sequence" VALUES ('django_content_type', 12);
INSERT INTO "sqlite_sequence" VALUES ('auth_permission', 48);
INSERT INTO "sqlite_sequence" VALUES ('auth_group', 0);
INSERT INTO "sqlite_sequence" VALUES ('auth_user', 1);
INSERT INTO "sqlite_sequence" VALUES ('Aconchego_hotel', 4);
INSERT INTO "sqlite_sequence" VALUES ('Aconchego_hotel_fotos', 8);
INSERT INTO "sqlite_sequence" VALUES ('Aconchego_reserva', 4);
INSERT INTO "sqlite_sequence" VALUES ('Aconchego_comment', 13);

-- ----------------------------
-- Auto increment value for Aconchego_comment
-- ----------------------------
UPDATE "sqlite_sequence" SET seq = 13 WHERE name = 'Aconchego_comment';

-- ----------------------------
-- Auto increment value for Aconchego_hotel
-- ----------------------------
UPDATE "sqlite_sequence" SET seq = 4 WHERE name = 'Aconchego_hotel';

-- ----------------------------
-- Auto increment value for Aconchego_hotel_fotos
-- ----------------------------
UPDATE "sqlite_sequence" SET seq = 8 WHERE name = 'Aconchego_hotel_fotos';

-- ----------------------------
-- Indexes structure for table Aconchego_hotel_fotos
-- ----------------------------
CREATE INDEX "Aconchego_hotel_fotos_hotel_id_a144ddaa"
ON "Aconchego_hotel_fotos" (
  "hotel_id" ASC
);

-- ----------------------------
-- Auto increment value for Aconchego_reserva
-- ----------------------------
UPDATE "sqlite_sequence" SET seq = 4 WHERE name = 'Aconchego_reserva';

-- ----------------------------
-- Indexes structure for table Aconchego_reserva
-- ----------------------------
CREATE INDEX "Aconchego_reserva_hotel_id_68cd4f1b"
ON "Aconchego_reserva" (
  "hotel_id" ASC
);

-- ----------------------------
-- Auto increment value for auth_group
-- ----------------------------

-- ----------------------------
-- Indexes structure for table auth_group_permissions
-- ----------------------------
CREATE INDEX "auth_group_permissions_group_id_b120cbf9"
ON "auth_group_permissions" (
  "group_id" ASC
);
CREATE UNIQUE INDEX "auth_group_permissions_group_id_permission_id_0cd325b0_uniq"
ON "auth_group_permissions" (
  "group_id" ASC,
  "permission_id" ASC
);
CREATE INDEX "auth_group_permissions_permission_id_84c5c92e"
ON "auth_group_permissions" (
  "permission_id" ASC
);

-- ----------------------------
-- Auto increment value for auth_permission
-- ----------------------------
UPDATE "sqlite_sequence" SET seq = 48 WHERE name = 'auth_permission';

-- ----------------------------
-- Indexes structure for table auth_permission
-- ----------------------------
CREATE INDEX "auth_permission_content_type_id_2f476e4b"
ON "auth_permission" (
  "content_type_id" ASC
);
CREATE UNIQUE INDEX "auth_permission_content_type_id_codename_01ab375a_uniq"
ON "auth_permission" (
  "content_type_id" ASC,
  "codename" ASC
);

-- ----------------------------
-- Auto increment value for auth_user
-- ----------------------------
UPDATE "sqlite_sequence" SET seq = 1 WHERE name = 'auth_user';

-- ----------------------------
-- Indexes structure for table auth_user_groups
-- ----------------------------
CREATE INDEX "auth_user_groups_group_id_97559544"
ON "auth_user_groups" (
  "group_id" ASC
);
CREATE INDEX "auth_user_groups_user_id_6a12ed8b"
ON "auth_user_groups" (
  "user_id" ASC
);
CREATE UNIQUE INDEX "auth_user_groups_user_id_group_id_94350c0c_uniq"
ON "auth_user_groups" (
  "user_id" ASC,
  "group_id" ASC
);

-- ----------------------------
-- Indexes structure for table auth_user_user_permissions
-- ----------------------------
CREATE INDEX "auth_user_user_permissions_permission_id_1fbb5f2c"
ON "auth_user_user_permissions" (
  "permission_id" ASC
);
CREATE INDEX "auth_user_user_permissions_user_id_a95ead1b"
ON "auth_user_user_permissions" (
  "user_id" ASC
);
CREATE UNIQUE INDEX "auth_user_user_permissions_user_id_permission_id_14a6b632_uniq"
ON "auth_user_user_permissions" (
  "user_id" ASC,
  "permission_id" ASC
);

-- ----------------------------
-- Auto increment value for django_admin_log
-- ----------------------------

-- ----------------------------
-- Indexes structure for table django_admin_log
-- ----------------------------
CREATE INDEX "django_admin_log_content_type_id_c4bce8eb"
ON "django_admin_log" (
  "content_type_id" ASC
);
CREATE INDEX "django_admin_log_user_id_c564eba6"
ON "django_admin_log" (
  "user_id" ASC
);

-- ----------------------------
-- Auto increment value for django_content_type
-- ----------------------------
UPDATE "sqlite_sequence" SET seq = 12 WHERE name = 'django_content_type';

-- ----------------------------
-- Indexes structure for table django_content_type
-- ----------------------------
CREATE UNIQUE INDEX "django_content_type_app_label_model_76bd3d3b_uniq"
ON "django_content_type" (
  "app_label" ASC,
  "model" ASC
);

-- ----------------------------
-- Auto increment value for django_migrations
-- ----------------------------
UPDATE "sqlite_sequence" SET seq = 26 WHERE name = 'django_migrations';

-- ----------------------------
-- Indexes structure for table django_session
-- ----------------------------
CREATE INDEX "django_session_expire_date_a5c62663"
ON "django_session" (
  "expire_date" ASC
);

PRAGMA foreign_keys = true;
