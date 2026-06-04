// Fake API - Base de datos en memoria
let fakeUsers = [
    { id: 1, email: "admin@ejemplo.com", password: "123456", name: "Administrador", role: "admin" },
    { id: 2, email: "user@ejemplo.com", password: "123456", name: "Usuario Normal", role: "user" }
];

let nextId = 3;

function delay(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

export const fakeAPI = {
    async getUsers() {
        await delay(200);
        return [...fakeUsers];
    },
    
    async getUser(id) {
        await delay(100);
        const user = fakeUsers.find(u => u.id === id);
        return user ? { ...user } : null;
    },
    
    async createUser(userData) {
        await delay(300);
        const newUser = { ...userData, id: nextId++ };
        fakeUsers.push(newUser);
        return { ...newUser };
    },
    
    async updateUser(id, userData) {
        await delay(300);
        const index = fakeUsers.findIndex(u => u.id === id);
        if (index !== -1) {
            fakeUsers[index] = { ...fakeUsers[index], ...userData };
            return { ...fakeUsers[index] };
        }
        throw new Error("Usuario no encontrado");
    },
    
    async deleteUser(id) {
        await delay(200);
        const index = fakeUsers.findIndex(u => u.id === id);
        if (index !== -1) {
            fakeUsers.splice(index, 1);
            return { success: true };
        }
        throw new Error("Usuario no encontrado");
    }
};