BEGIN;
--
-- Create model Article
--
CREATE TABLE "article_article" ("articleID" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "postDate" datetime NOT NULL, "category" varchar(120) NOT NULL, "title" varchar(120) NOT NULL, "imagesPath" varchar(100) NOT NULL, "preamble" text NOT NULL);
--
-- Create model Section
--
CREATE TABLE "article_section" ("sectionId" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(120) NOT NULL, "secText" text NOT NULL, "hasSubSections" bool NOT NULL, "article_id" integer NOT NULL REFERENCES "article_article" ("articleID") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model SubSection
--
CREATE TABLE "article_subsection" ("sectionId" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(120) NOT NULL, "subSecText" text NOT NULL, "section_id" integer NOT NULL REFERENCES "article_section" ("sectionId") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "article_section_article_id_567119be" ON "article_section" ("article_id");
CREATE INDEX "article_subsection_section_id_23ffecb9" ON "article_subsection" ("section_id");
COMMIT;
