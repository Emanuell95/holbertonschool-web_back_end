class Currency {
        constructor(code, name) {
            this._code = code;
            this._name = name;
        }
    
        get code() {
            return this._code;
        }
        set code(code) {
            if (typeof code !== 'string') {
                throw new TypeError('Code must be a string');
            }
            this._code = code;
        }
        get name() {
            return this._name;
        }
        set name(name) {
            this._name = name;
        }
    
        displayFullCurrency() {
            return `${this._name} (${this._code})`;
        }
    }
export default Currency;
        
