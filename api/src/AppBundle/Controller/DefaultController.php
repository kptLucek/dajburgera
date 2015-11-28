<?php

namespace AppBundle\Controller;

use AppBundle\Entity\Restaurant;
use Doctrine\DBAL\Exception\UniqueConstraintViolationException;
use FOS\RestBundle\Controller\Annotations as Rest;
use FOS\RestBundle\Controller\FOSRestController;
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\Response;

class DefaultController extends FOSRestController
{

    /**
     * @param Request $request
     * @Rest\Get("/get-burgers")
     *
     * @return Response
     */
    public function getBurgersAction(Request $request)
    {
        $view = $this->view([
            'status' => 'ok',
            'code' => 200,
//            'data' => $this->get('fos_elastica.finder.burger.restaurant')->find();
        ]);
        return $this->handleView($view);
    }

    /**
     * @param Request $request
     * @Rest\Put("/put-burger")
     *
     * @return Response
     */
    public function putBurgerAction(Request $request)
    {
        try {
            $postParams = $request->request->all();
            $validator = $this->get('validator');
            $propertyAccessor = $this->get('property_accessor');
            $entry = new Restaurant();
            foreach ($postParams as $key => $value) {
                if (false === $propertyAccessor->isWritable($entry, $key)) {
                    return $this->handleView($this->view([
                        'status' => 'error',
                        'code' => Response::HTTP_METHOD_NOT_ALLOWED,
                        'message' => sprintf('Property "%s" is not recognized.', $key)
                    ]));
                }
                $propertyAccessor->setValue($entry, $key, $value);
                $propertyValid = $validator->validateProperty($entry, $key);
                if (0 < $propertyValid->count()) {
                    return $this->handleView($this->view($propertyValid));
                }
            }
            try {
                $em = $this->get('doctrine.orm.default_entity_manager');
                $em->persist($entry);
                $em->flush($entry);
                $elastica = $this->get('fos_elastica.index.burger.restaurant');
                $elastica->addObject($entry);
            } catch (UniqueConstraintViolationException $exception) {
                return $this->handleView($this->view([
                    'status' => 'error',
                    'code' => Response::HTTP_BAD_REQUEST,
                    'message' => 'Already in database.'
                ]));
            }
        }catch(\Exception $e){
            return $this->handleView($this->view([
                'status' => 'error',
                'code' => Response::HTTP_BAD_REQUEST,
                'message' => 'Unknown error :).'
            ]));
        }
        return $this->handleView($this->view([
            'status' => 'ok',
            'code' => Response::HTTP_OK
        ]));
    }
}
