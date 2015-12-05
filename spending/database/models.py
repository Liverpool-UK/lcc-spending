# coding=UTF-8

import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, DateTime, Unicode, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Over500(Base):
    __tablename__ = 'over500'
    id = Column(Integer, primary_key=True)

    service_area     = Column(Unicode, nullable=True)
    expense_type   = Column(Unicode, nullable=True)
    sap_document  = Column(Unicode, index=True)
    posting_date = Column(DateTime)
    vendor  = Column(Unicode, nullable=True)
    amount  = Column(Float, nullable=True)
    month  = Column(Integer)
    year  = Column(Float)

    def __repr__(self):
        return self.__unicode__()

    def __unicode__(self):
        return u'{0} paid {1} GBP{2}'.format(self.service_area, self.vendor, self.amount)