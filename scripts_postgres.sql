-- criar view para ver todas as tabelas do banco
CREATE VIEW tabelas AS SELECT table_name AS Todas_as_Tabelas
FROM information_schema.tables
WHERE table_schema='public'
AND table_type='BASE TABLE';

-- select com a view já criada
SELECT todas_as_tabelas
	FROM public.tabelas;

-- select com titulos a patir de 1900 usando LIMIT de 10 linhas e organizando em ordem descrescente

SELECT series_years as ano, title as titulo
 FROM title
 WHERE series_years 
 like '19%'
 ORDER BY series_years DESC
 LIMIT 10;

-- view de titulos a partir de 1900
SELECT ano, titulo
	FROM public.filmes_1900;