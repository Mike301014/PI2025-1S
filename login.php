<?php
session_start();

// Conexão ao banco
$host = 'localhost';
$db = 'database';
$user = 'user';
$pass = 'password';

$conn = new mysqli($host, $user, $pass, $db);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// form data
$username = $_POST['username'];
$password = $_POST['password'];

// Proteção SQL injection
$username = $conn->real_escape_string($username);
$password = $conn->real_escape_string($password);

// Query para verificar credenciais
$sql = "SELECT * FROM users WHERE username = '$username'";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    $row = $result->fetch_assoc();
    if (password_verify($password, $row['password'])) {
        // A senha está correta, inicie uma nova sessão
        $_SESSION['username'] = $username;
        echo "Login efetuado com sucesso!";
        // Redirecionar para uma página segura
        header("Location: home.php");
    } else {
        echo "Senha inválida!";
    }
} else {
    echo "Usuário não encontrado!";
}

$conn->close();
?>
