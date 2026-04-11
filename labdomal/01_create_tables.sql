-- =========================
-- BANCO CLINICA (SIMPLES)
-- =========================

-- PACIENTES
CREATE TABLE pacientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    cpf TEXT UNIQUE,
    telefone TEXT,
    email TEXT,
    data_nascimento DATE
);

-- MÉDICOS
CREATE TABLE medicos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    especialidade TEXT,
    crm TEXT UNIQUE
);

-- ESTAGIARIOS
CREATE TABLE estagiarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    cpf TEXT UNIQUE,
    telefone TEXT,
    email TEXT,
    curso TEXT,
    instituicao TEXT,
    data_inicio DATE,
    data_fim DATE,
    carga_horaria INTEGER,
    bolsa NUMERIC
);

-- USUÁRIOS (login do sistema)
CREATE TABLE usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    email TEXT UNIQUE,
    senha TEXT,
    tipo TEXT -- admin, medico, recepcao
);

-- CONSULTAS
CREATE TABLE consultas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    paciente_id INTEGER,
    medico_id INTEGER,
    data DATE,
    hora TEXT,
    status TEXT, -- agendada, realizada, cancelada
    observacoes TEXT,

    FOREIGN KEY (paciente_id) REFERENCES pacientes(id),
    FOREIGN KEY (medico_id) REFERENCES medicos(id)
);

-- PRONTUÁRIO
CREATE TABLE prontuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    consulta_id INTEGER UNIQUE,
    diagnostico TEXT,
    prescricao TEXT,
    observacoes TEXT,

    FOREIGN KEY (consulta_id) REFERENCES consultas(id)
);