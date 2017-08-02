// Usage: mongo < card_data.js
use chocobros;
//db.createCollection("cards");
db.cards.insertMany([
    {
        name: 'Auron',
        cost: '6',
        element: 'fire',
        type: 'forward',
        job: 'Guardian',
        category: 'X',
        text: 'When Auron deals damage to your opponent, you may play 1 Fire Backup from your hand onto the field dull',
        rarity: 'H',
        power: '9000',
        set: '1',
        number: '1'
    },
    {
        name: 'Auron',
        cost: '5',
        element: 'fire',
        type: 'forward',
        job: 'Guardian',
        category: 'X',
        text: 'The Backups you control cannot be broken by your opponent\'s Summons or abilities',
        rarity: 'H',
        power: '9000',
        set: '1',
        number: '2'
    },
    {
        name: 'Red Mage',
        cost: '2',
        element: 'fire',
        type: 'backup',
        job: 'Standard Unit',
        category: 'III',
        text: 'Choose 1 Forward. It cannot block this turn.',
        rarity: 'C',
        set: '1',
        number: '3'
    }
]);
