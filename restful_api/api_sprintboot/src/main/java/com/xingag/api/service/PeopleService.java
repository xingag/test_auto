package com.xingag.api.service;

import com.xingag.api.domain.People;

import java.util.List;

/***
 * 对外提供的接口
 */
public interface PeopleService {
    //获取所有的数据
    List<People> getAllPeoples();

    //获取某一条记录
    People getOnePeople(int id);

    //更新一条记录
    boolean updatePeople(People people);

    //新增一条记录
    boolean addPeople(People people);

    //删除一条记录
    boolean delPeople(int id);

}
