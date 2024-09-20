import postgres from 'postgres'

const sql = postgres("postgres://default_user:qwerty123!@postgresdb:5432/api_database") // will use psql environment variables

console.log(sql)

export default sql
