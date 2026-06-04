import { checkAdmin } from './helpers.js';

const API_URL = 'http://localhost:3000/users';
let allUsers = [];

const adminUser = checkAdmin();
if (!adminUser) return;

document.addEventListener('DOMContentLoaded', () => {
    loadUsers();
    document.getElementById('createUserBtn').addEventListener('click', openCreateModal);
    document.getElementById('closeModalBtn').addEventListener('click', closeModal);
    document.getElementById('userForm').addEventListener('submit', saveUser);
    document.getElementById('logoutBtn').addEventListener('click', logout);
});

async function loadUsers() {
    try {
        const response = await fetch(API_URL);
        allUsers = await response.json();
        renderUsers();
    } catch (error) {
        alert('Error al cargar usuarios');
    }
}

function renderUsers() {
    const tbody = document.getElementById('usersTableBody');
    
    if (allUsers.length === 0) {
        tbody.innerHTML = '<tr><td colspan="5" class="text-center py-4">No hay usuarios</td></tr>';
        return;
    }
    
    tbody.innerHTML = allUsers.map(user => `
        <tr class="border-b">
            <td class="px-4 py-2">${user.id}</td>
            <td class="px-4 py-2">${user.name}</td>
            <td class="px-4 py-2">${user.email}</td>
            <td class="px-4 py-2">${user.role === 'admin' ? 'Admin' : 'Usuario'}</td>
            <td class="px-4 py-2">
                <button onclick="editUser(${user.id})" class="bg-yellow-500 text-white px-2 py-1 rounded text-sm">Editar</button>
                <button onclick="deleteUser(${user.id})" class="bg-red-500 text-white px-2 py-1 rounded text-sm">Eliminar</button>
            </td>
        </tr>
    `).join('');
}

window.editUser = async (id) => {
    const user = allUsers.find(u => u.id === id);
    if (user) {
        document.getElementById('modalTitle').textContent = 'Editar Usuario';
        document.getElementById('userId').value = user.id;
        document.getElementById('userName').value = user.name;
        document.getElementById('userEmail').value = user.email;
        document.getElementById('userRole').value = user.role;
        document.getElementById('userPassword').value = '';
        document.getElementById('userModal').classList.remove('hidden');
        document.getElementById('userModal').classList.add('flex');
    }
};

window.deleteUser = async (id) => {
    if (confirm('¿Eliminar este usuario?')) {
        try {
            await fetch(`${API_URL}/${id}`, { method: 'DELETE' });
            loadUsers();
        } catch (error) {
            alert('Error al eliminar');
        }
    }
};

function openCreateModal() {
    document.getElementById('modalTitle').textContent = 'Crear Usuario';
    document.getElementById('userForm').reset();
    document.getElementById('userId').value = '';
    document.getElementById('userModal').classList.remove('hidden');
    document.getElementById('userModal').classList.add('flex');
}

function closeModal() {
    document.getElementById('userModal').classList.add('hidden');
    document.getElementById('userModal').classList.remove('flex');
}

async function saveUser(e) {
    e.preventDefault();
    const id = document.getElementById('userId').value;
    const userData = {
        name: document.getElementById('userName').value,
        email: document.getElementById('userEmail').value,
        role: document.getElementById('userRole').value
    };
    
    const password = document.getElementById('userPassword').value;
    if (password) userData.password = password;
    
    try {
        if (id) {
            await fetch(`${API_URL}/${id}`, {
                method: 'PUT',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(userData)
            });
        } else {
            userData.password = password || '123456';
            await fetch(API_URL, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(userData)
            });
        }
        closeModal();
        loadUsers();
    } catch (error) {
        alert('Error al guardar');
    }
}

function logout() {
    localStorage.removeItem('user');
    window.location.href = 'index.html';
}