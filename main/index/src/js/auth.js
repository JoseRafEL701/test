const API_URL = 'http://localhost:3000/users';

document.getElementById('loginForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const errorDiv = document.getElementById('errorMessage');
    
    errorDiv.classList.add('hidden');
    
    try {
        const response = await fetch(API_URL);
        const users = await response.json();
        
        const user = users.find(u => u.email === email && u.password === password);
        
        if (user) {
            const sessionUser = {
                id: user.id,
                email: user.email,
                name: user.name,
                role: user.role
            };
            localStorage.setItem('user', JSON.stringify(sessionUser));
            
            if (user.role === 'admin') {
                window.location.href = 'admin.html';
            } else {
                window.location.href = 'user.html';
            }
        } else {
            errorDiv.textContent = 'Email o contraseña incorrectos';
            errorDiv.classList.remove('hidden');
        }
    } catch (error) {
        errorDiv.textContent = 'Error al conectar con el servidor';
        errorDiv.classList.remove('hidden');
    }
});