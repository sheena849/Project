from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from db_setup import Base
from datetime import datetime

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True)
    type = Column(String, nullable=False)  # e.g., "buy" or "sell"
    amount = Column(Float, nullable=False)
    investment_id = Column(Integer, ForeignKey("investments.id"))
    portfolio_id = Column(Integer, ForeignKey("portfolios.id"))  # Add this line for the foreign key
    date = Column(DateTime, default=datetime.utcnow)  # Date and time of the transaction
    notes = Column(String)  # Optional field for additional information

    # Relationships
    investment = relationship("Investment", back_populates="transactions")
    portfolio = relationship("Portfolio", back_populates="transactions")  # Ensure this relationship is present

    def __repr__(self):
        return (
            f"Transaction(id={self.id}, type='{self.type}', amount={self.amount}, "
            f"date={self.date}, notes='{self.notes}')"
        )
