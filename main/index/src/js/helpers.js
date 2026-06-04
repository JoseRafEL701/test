export function checkAuth() {
    const user = localStorage.getItem('user');
    if (!user) {
        window.location.href = 'index.html';
        return null;
    }
    return JSON.parse(user);
}

export function checkAdmin() {
    const user = checkAuth();
    if (!user || user.role !== 'admin') {
        alert('No tienes permiso');
        window.location.href = 'user.html';
        return null;
    }
    return user;
}