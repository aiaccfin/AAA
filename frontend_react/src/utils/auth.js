export function decodeToken(token) {
    const parts = token.split('.');
    if (parts.length !== 3) {
        throw new Error("Invalid token format");
    }
    
    return JSON.parse(atob(parts[1])); // Decode Base64 payload
}
