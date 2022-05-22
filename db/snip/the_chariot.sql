SELECT id, BIN_TO_UUID(id), name FROM tarot.card;

/*INSERT INTO tarot.card (id, name) SELECT UUID_TO_BIN(UUID()), "the chariot"