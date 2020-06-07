package com.xingag.api.service;

import com.xingag.api.domain.People;
import com.xingag.api.handle.PeopleHandle;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class PeopleServiceImp implements PeopleService {

    //导入
    @Autowired
    private PeopleHandle peopleHandle;


    @Override
    public List<People> getAllPeoples() {
        return peopleHandle.getAllPeople();
    }

    @Override
    public People getOnePeople(int id) {
        return peopleHandle.getPeople(id);
    }

    @Override
    public boolean updatePeople(People people) {
        return peopleHandle.updatePeople(people) > 0;
    }

    @Override
    public boolean addPeople(People people) {
        return peopleHandle.insertPeople(people.getName(),people.getAge(),people.isExtra())>0;
    }

    @Override
    public boolean delPeople(int id) {
        return peopleHandle.deletePeople(id)>0;
    }
}
