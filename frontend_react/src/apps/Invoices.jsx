import React, { useEffect, useState } from 'react';
import { MDBContainer, MDBCard, MDBCardBody, MDBCardTitle, MDBCardText } from 'mdb-react-ui-kit';

function Invoices() {
    const [invoices, setInvoices] = useState([]);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchInvoices = async () => {
            try {
                const response = await fetch('http://localhost:8080/invoice/list');
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }

                const data = await response.json();
                setInvoices(data);
            } catch (err) {
                console.error('Failed to fetch invoices:', err);
                setError('Failed to load invoices.');
            }
        };

        fetchInvoices();
    }, []);

    const handleSendReminder = async (vendor, invoiceNumber, dueDate, balanceDue) => {
        try {
            const response = await fetch('http://localhost:8080/invoice/email-reminder', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    vendor: vendor,
                    invoice_number: invoiceNumber,
                    due_date: dueDate,
                    balance_due: balanceDue
                })
            });

            if (!response.ok) {
                const err = await response.json();
                throw new Error(err.detail || 'Failed to send reminder');
            }

            alert(`Reminder sent for Invoice #${invoiceNumber}`);
        } catch (err) {
            console.error('Error sending reminder:', err);
            alert(`Error: ${err.message}`);
        }
    };

    return (
        <MDBContainer className="p-3 my-5">
            <h2>Invoice List</h2>
            {error && <p style={{ color: 'red' }}>{error}</p>}

            {invoices.map((inv, index) => (
                <MDBCard className="mb-4" key={inv._id || index}>
                    <MDBCardBody>
                        <MDBCardTitle>Invoice #{inv.invoice_number}</MDBCardTitle>
                        <MDBCardText>
                            <strong>Vendor:</strong> {inv.vendor}<br />
                            <strong>Invoice To:</strong> {inv.invoice_to}<br />
                            <strong>Address:</strong> {inv.address}<br />
                            <strong>Service Period:</strong> {inv.date}<br />
                            <strong>Due Date:</strong> {inv.due_date}<br />
                            <strong>Terms:</strong> {inv.terms}<br />
                            <strong>Service:</strong> {inv.service_description}<br />
                            <strong>Items:</strong>
                            <ul>
                                {inv.items.map((item, i) => (
                                    <li key={i}>
                                        {item.description} — {item.quantity} x ${item.rate} = ${item.amount}
                                    </li>
                                ))}
                            </ul>
                            <strong>Subtotal:</strong> ${inv.subtotal}<br />
                            <strong>Tax:</strong> ${inv.tax}<br />
                            <strong>Total:</strong> <strong>${inv.total}</strong><br />
                            <strong>Balance Due:</strong> ${inv.balance_due}<br />
                            <em>{inv.message}</em>

                            <button
                                className="btn btn-primary"
                                onClick={() => handleSendReminder(inv.vendor, inv.invoice_number, inv.due_date, inv.balance_due)}
                            >
                                Email Reminder
                            </button>
                        </MDBCardText>
                    </MDBCardBody>
                </MDBCard>
            ))}
        </MDBContainer>
    );
}

export default Invoices;
