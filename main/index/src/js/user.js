import { checkAuth } from './helpers.js';

const API_URL = 'http://localhost:3000/users';

const currentUser = checkAuth();
if (!currentUser) return;

if (currentUser.role === 'admin') {
    window.location.href = 'admin.html';
}

let userData = null;

document.addEventListener('DOMContentLoaded', () => {
    loadProfile();
    document.getElementById('profileForm').addEventListener('submit', updateProfile);
    document.getElementById('logoutBtn').addEventListener('click', logout);
});

async function loadProfile() {
    try {
        const response = await fetch(`${API_URL}/${currentUser.id}`);
        userData = await response.json();
        
        document.getElementById('userName').value = userData.name;
        document.getElementById('userEmail').value = userData.email;
        document.getElementById('userRole').value = userData.role === 'admin' ? 'Administrador' : 'Usuario';
    } catch (error) {
        alert('Error al cargar perfil');
    }
}

async function updateProfile(e) {
    e.preventDefault();
    
    const updatedData = {
        name: document.getElementById('userName').value,
        email: document.getElementById('userEmail').value,
        role: userData.role,
        password: userData.password
    };
    
    const newPassword = document.getElementById('userPassword').value;
    if (newPassword) {
        updatedData.password = newPassword;
    }
    
    try {
        await fetch(`${API_URL}/${currentUser.id}`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(updatedData)
        });
        
        const sessionUser = {
            id: currentUser.id,
            email: updatedData.email,
            name: updatedData.name,
            role: currentUser.role
        };
        localStorage.setItem('user', JSON.stringify(sessionUser));
        
        alert('Perfil actualizado');
        document.getElementById('userPassword').value = '';
    } catch (error) {
        alert('Error al actualizar');
    }
}

function logout() {
    localStorage.removeItem('user');
    window.location.href = 'index.html';
}