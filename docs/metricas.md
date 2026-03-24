# Métricas de Negócio

## 1. Empresa com mais passageiros por ano
```sql
SELECT
    d.ano,
    e.nome_empresa,
    SUM(f.passageiros) AS total_passageiros
FROM fato_voos f
JOIN dim_data d ON f.data_id = d.data_id
JOIN dim_empresa e ON f.empresa_id = e.empresa_id
GROUP BY d.ano, e.nome_empresa
ORDER BY d.ano, total_passageiros DESC;
```

## 2. Aeroportos de origem com maior volume de voos
```sql
SELECT
    a.nome,
    a.cidade,
    SUM(f.quantidade_voos) AS total_voos
FROM fato_voos f
JOIN dim_aeroporto a ON f.aeroporto_origem_id = a.aeroporto_id
GROUP BY a.nome, a.cidade
ORDER BY total_voos DESC;
```

## 3. Região com maior movimentação de passageiros
```sql
SELECT
    a.regiao,
    SUM(f.passageiros) AS total_passageiros
FROM fato_voos f
JOIN dim_aeroporto a ON f.aeroporto_origem_id = a.aeroporto_id
WHERE a.regiao is not null
GROUP BY a.regiao
ORDER BY total_passageiros DESC;
```

## 4. Evolução mensal de passageiros
```sql
SELECT
    d.ano,
    d.mes,
    SUM(f.passageiros) AS total_passageiros
FROM fato_voos f
JOIN dim_data d ON f.data_id = d.data_id
GROUP BY d.ano, d.mes
ORDER BY d.ano, d.mes;
```

## 5. Média de passageiros por voo por empresa
```sql
SELECT
    e.nome_empresa,
    SUM(f.passageiros) / NULLIF(SUM(f.quantidade_voos),0) AS media_passageiros_por_voo
FROM fato_voos f
JOIN dim_empresa e ON f.empresa_id = e.empresa_id
GROUP BY e.nome_empresa
ORDER BY media_passageiros_por_voo DESC;
```
