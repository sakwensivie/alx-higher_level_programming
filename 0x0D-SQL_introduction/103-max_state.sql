-- max states

SELECT state, MAX(value)
FROM temperatures
GROUP BY state
LIMIT 3;