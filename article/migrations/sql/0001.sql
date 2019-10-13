BEGIN;
--
-- Create model Section
--
CREATE TABLE "article_section" ("sectionId" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(120) NOT NULL, "secText" text NOT NULL, "hasSubSections" bool NOT NULL);
--
-- Create model Topic
--
CREATE TABLE "article_topic" ("articleID" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "postDate" datetime NOT NULL, "category" varchar(120) NOT NULL, "title" varchar(120) NOT NULL, "imagesPath" varchar(100) NOT NULL, "preamble" text NOT NULL, "time_worst" varchar(1) NOT NULL, "time_average" varchar(1) NOT NULL, "time_best" varchar(1) NOT NULL, "space_worst" varchar(1) NOT NULL, "space_average" varchar(1) NOT NULL, "space_best" varchar(1) NOT NULL);
--
-- Create model SubSection
--
CREATE TABLE "article_subsection" ("subSectionId" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(120) NOT NULL, "subSecText" text NOT NULL, "section_id" integer NOT NULL REFERENCES "article_section" ("sectionId") DEFERRABLE INITIALLY DEFERRED);
--
-- Add field topic to section
--
CREATE TABLE "new__article_section" ("sectionId" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(120) NOT NULL, "secText" text NOT NULL, "hasSubSections" bool NOT NULL, "topic_id" integer NOT NULL REFERENCES "article_topic" ("articleID") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO "new__article_section" ("sectionId", "title", "secText", "hasSubSections", "topic_id") SELECT "sectionId", "title", "secText", "hasSubSections", NULL FROM "article_section";
DROP TABLE "article_section";
ALTER TABLE "new__article_section" RENAME TO "article_section";
CREATE INDEX "article_subsection_section_id_23ffecb9" ON "article_subsection" ("section_id");
CREATE INDEX "article_section_topic_id_8fd87e51" ON "article_section" ("topic_id");
--
-- Create model NotGoodFor
--
CREATE TABLE "article_notgoodfor" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "item1" varchar(120) NOT NULL, "item2" varchar(120) NOT NULL, "item3" varchar(120) NOT NULL, "item4" varchar(120) NOT NULL, "item5" varchar(120) NOT NULL, "topic_id" integer NOT NULL REFERENCES "article_topic" ("articleID") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model GoodFor
--
CREATE TABLE "article_goodfor" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "item1" varchar(120) NOT NULL, "item2" varchar(120) NOT NULL, "item3" varchar(120) NOT NULL, "item4" varchar(120) NOT NULL, "item5" varchar(120) NOT NULL, "topic_id" integer NOT NULL REFERENCES "article_topic" ("articleID") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "article_notgoodfor_topic_id_a2255f85" ON "article_notgoodfor" ("topic_id");
CREATE INDEX "article_goodfor_topic_id_186e8687" ON "article_goodfor" ("topic_id");
COMMIT;
